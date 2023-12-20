from django.shortcuts import render

# Create your views here.
def contact(req):
    return render(req,'navigation/contact.html')
def about(req):
    return render(req,'navigation/about.html')
