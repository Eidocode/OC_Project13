from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash, \
    authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from users.forms import SignupForm, LoginForm, ChangePasswordForm, \
    ResetPasswordForm, ResetPasswordConfirmForm, ChangeFullnameForm
from users.token import token_generator


def login_page(request):
    """
    View used for user login
    """
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Checks user authentication
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            # If user is authenticated, redirect to home page
            if user is not None:
                login(request, user)
                messages.success(request, f'{user.username}est connecté...')
                return redirect('/')
        else:
            # If user is not authenticated, display an error and reload form
            for error in list(form.errors.values()):
                messages.error(request, error)
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    """
    View used for user registration
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # Save user but not commit to database
            user = form.save(commit=False)
            # Set user status to inactive
            user.is_active = False
            # Save user to database
            user.save()
            # Send activation email
            activate_mail(request, user, form.cleaned_data.get('email'))
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    """
    View used for user activation

    :param uidb64: UID of the user
    :param token: Token generated
    """
    user_model = get_user_model()
    try:
        # Decode the UID
        uid = force_str(urlsafe_base64_decode(uidb64))
        # Get user from the model
        user = user_model.objects.get(pk=uid)
    except:
        user = None

    # If user and token is valid, activate user and redirect to login page
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Merci d'avoir confirmé votre compte. Vous \
            pouvez maintenant vous connecter")
        return redirect('login')

    messages.error(request, "Le lien d'activation n'est plus valide...")
    return redirect('/')


def activate_mail(request, user, to_email):
    """
    View used for user activation mail

    :param user: User object
    :param to_email: Email address of the user
    """
    mail_subject = '[NO-REPLY] Activer votre compte OC-Inventory'
    # Data to insert in the template
    data_to_insert = {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    }
    # Render in plain text and html formats
    message_plain_text = render_to_string(
        'users/mails/mail_activate_account_fulltext.html', data_to_insert)
    message_html = render_to_string('users/mails/mail_activate_account.html',
                                    data_to_insert)
    email = EmailMultiAlternatives(mail_subject, message_plain_text,
                                   to=[to_email])
    email.attach_alternative(message_html, "text/html")

    # Send email
    if email.send():
        messages.success(request, f"Cher <b>{user}</b>, merci de cliquer sur \
                    le lien d'activation, dans votre boîte mail pour \
                    confirmer et compléter le processus d'enregistrement.")
    else:
        messages.error(request, f"Problème lors de l'envoi de l'email à \
            l'adresse {to_email}, vérifiez que la saisie est correcte...")


@login_required
def account(request):
    """
    View used for user account page
    """
    return render(request, 'users/account/account.html')


@login_required
def change_fullname(request):
    """
    View used for user change firstname and lastname
    """
    form = ChangeFullnameForm()
    if request.method == 'POST':
        form = ChangeFullnameForm(data=request.POST, instance=request.user)
        if form.is_valid():
            # Save user information and redirect to account
            form.save()
            messages.success(request,
                             'Vos informations ont été mises à jour...')
            return redirect('account')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    return render(request, 'users/account/change_fullname.html', {
        'form': form})


@login_required
def change_password(request):
    """
    View used for user change password
    """
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            # Save user model and redirect to account
            user = form.save()
            # Update user session with new password
            update_session_auth_hash(request, user)
            messages.success(request, 'Mot de passe modifié avec succès...')
            return redirect('account')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = ChangePasswordForm(request.user)
    return render(request, 'users/account/change_password.html', {
        'form': form,
    })


def reset_password(request):
    """
    View used for user reset password
    """
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            # Get email form cleaned data
            user_email = form.cleaned_data['email']
            # Get associated user model
            associated_user = get_user_model().objects.filter(
                email=user_email).first()
            # If associated user is not found, display an error and reload form
            if associated_user:
                mail_subject = '[NO-REPLY] Réinitialiser votre mot de passe'
                # Data to insert in the template
                datas = {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(
                        associated_user.pk)
                    ),
                    'token': token_generator.make_token(associated_user),
                    'protocol': 'https' if request.is_secure() else 'http'
                }
                # Render in plain text and html formats
                message_plain_text = render_to_string(
                    'users/mails/mail_reset_password_fulltext.html', datas)
                message_html = render_to_string(
                    'users/mails/mail_reset_password.html', datas)
                email = EmailMultiAlternatives(mail_subject,
                                               message_plain_text,
                                               to=[associated_user.email])
                email.attach_alternative(message_html, "text/html")

                if email.send():
                    messages.success(
                        request,
                        "Email envoyé avec succès, consultez votre boîte mail."
                    )
                    return redirect('login')
                else:
                    messages.error(
                        request, "Problème lors de l'envoi de l'email \
                        nécessaire pour engager la réinitialisation du mot de \
                        passe...")

    form = ResetPasswordForm()
    return render(
        request,
        'registration/password_reset_form.html',
        {'form': form}
    )


def reset_password_confirm(request, uidb64, token):
    """
    View used for user reset password confirm

    :param uidb64: UID of the user
    :param token: Token generated
    """
    # Get user model
    user_model = get_user_model()
    try:
        # Decode the UID
        uid = force_str(urlsafe_base64_decode(uidb64))
        # Get associated user model with uid
        user = user_model.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        if request.method == 'POST':
            form = ResetPasswordConfirmForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Le mot de passe a été modifié...")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        form = ResetPasswordConfirmForm(user)
        return render(
            request,
            'registration/password_reset_confirm.html',
            {'form': form}
        )
    else:
        messages.error(request, 'Le lien a expiré...')

    return redirect('login')
