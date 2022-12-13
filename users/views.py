from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
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
            activate_email(request, user, form.cleaned_data.get('email'))
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})


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


def activate_email(request, user, to_email):
    mail_subject = "Activate your OC-Inventory account"
    message = render_to_string('users/activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please, click on \
                    received activation link to confirm and complete the \
                    registration process.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check \
            if you tiped it correctly.')


def account(request):
    """
    Used for user account page
    """
    return render(request, 'users/account.html')
