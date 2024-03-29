from django.shortcuts import render, redirect
from django.contrib import messages as django_messages
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            django_messages.info(request, "username already exists")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            django_messages.info(request, "email already exists")
            return redirect("register")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            mydict = {'username': username}
            user.save()
            html_template = 'register_email.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Welcome to xudayfi`s house'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            email_msg = EmailMessage(subject, html_message, email_from, recipient_list)
            email_msg.content_subtype = 'html'
            email_msg.send()
            return redirect('success')
    else:
        return render(request, 'register.html')

def success(request):
    return render(request, "success.html")
