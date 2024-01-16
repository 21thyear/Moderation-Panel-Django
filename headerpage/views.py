from django.shortcuts import render
from django.core.mail import send_mail

def headerPage(request):
    send_mail(
        "Your project",
        "Your project is a good!",
        None,
        ["scottdale.attorney@gmail.com"],
    )
    return render(request, 'headerpage/header.html', {})