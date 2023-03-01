from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from product.forms import ContactUsForm
from product.models import Device
from tools import const


def index(request):
    """
    Used for index page
    """
    devices = Device.objects.filter().order_by('-added_date')[:5]
    current_user = request.user

    labels = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet"]
    datas = [150, 200, 250, 300, 350, 400, 450]

    context = {
        'devices': devices,
        'labels': labels,
        'datas': datas,
    }
    return render(request, 'product/index.html', context)


def contact_us(request):
    """
    Used for contact us page
    """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            data_form = {
                'f_name': form.cleaned_data['first_name'],
                'l_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
                'user': request.user,
            }
            mail_subject = f"[CONTACT] Requête de {data_form['f_name']} {data_form['l_name']} "
            message_plain_text = render_to_string('product/contact_us/request_contact_us_fulltext.html', data_form)
            message_html = render_to_string('product/contact_us/request_contact_us.html', data_form)
            email = EmailMultiAlternatives(
                mail_subject, message_plain_text, to=[const.EMAIL_HOST_USER])
            email.attach_alternative(message_html, "text/html")

            if email.send():
                messages.success(request, f"{data_form['f_name']}, votre message a été envoyé avec succès...")
                return redirect('contact_us')
            else:
                messages.error(request, "Votre message n'a pas pu être envoyé...")

    form = ContactUsForm()
    return render(request, 'product/contact_us/contact_us.html', {'form': form})
