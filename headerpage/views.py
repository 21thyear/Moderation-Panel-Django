from django.shortcuts import render

def header(request):
    return render(request, 'headerpage/header.html', {})