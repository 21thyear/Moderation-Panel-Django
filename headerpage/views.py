from django.shortcuts import render

def headerPage(request):
    return render(request, 'headerpage/header.html', {})