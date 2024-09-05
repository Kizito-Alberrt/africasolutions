from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def blog(request):
    return render(request,'blog.html',{})

def service(request):
    return render(request,'service.html',{})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        name = request.POST['name']
        send_email(
            message_name,
            message,
            message_email,
            ['wagabi98@@gmail.com'],
            
        )
    return render(request,'contact.html',{})