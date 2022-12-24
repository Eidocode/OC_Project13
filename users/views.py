from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from users.forms import SignupForm
from users.token import token_generator


def signup(request):
    """
    Used for user registration
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activate_mail(request, user, form.cleaned_data.get('email'))
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SignupForm()

    return render(request, 'users/account/signup.html', {'form': form})


def activate(request, uidb64, token):
    user_model = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user_model.objects.get(pk=uid)
    except:
        user = None

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for email confirmation. Now, \
            you can login to your account.')
        return redirect('login')

    messages.error(request, 'Activation link is invalid...')
    return redirect('/')


def activate_mail(request, user, to_email):
    mail_subject = "Activate your OC-Inventory account"
    data_to_insert = {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    }
    message_plain_text = render_to_string(
        'users/mails/mail_activate_account_fulltext.html', data_to_insert)
    message_html = render_to_string('users/mails/mail_activate_account.html', data_to_insert)
    email = EmailMultiAlternatives(mail_subject, message_plain_text, to=[to_email])
    email.attach_alternative(message_html, "text/html")

    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please, click on \
                    received activation link to confirm and complete the \
                    registration process.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check \
            if you typed it correctly.')


def account(request):
    """
    Used for user account page
    """
    return render(request, 'users/account/account.html')


def change_password(request):
    """
    Used when user change his password
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update user session with new password
            update_session_auth_hash(request, user)
            messages.success(request, 'The password has been successfully changed.')
            return redirect('account')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = PasswordChangeForm(request.user)
    return render(request, 'users/account/change_password.html', {
        'form': form,
    })


def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(email=user_email).first()
            if associated_user:
                subject = 'Password reset request'
                message = render_to_string("users/mails/mail_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': token_generator.make_token(associated_user),
                    'protocol': 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request, "Email sent successfully, check your mailbox")
                    return redirect('login')
                else:
                    messages.error(request, "Problem sending reset password email")

    form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})


def reset_password_confirm(request, uidb64, token):
    UserModel = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been set. You may go ahead and <b>log in</b> now.')
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'registration/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, 'Link is expired...')

    return redirect('login')
