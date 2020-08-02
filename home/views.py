from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"PK is great",
        "variable2":"He is a good coder"
    }
    return render(request, 'index.html', context)
    # return HttpResponse('This is a homepage...')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is about homepage...')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('This is services homepage...')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        # Contact object creation
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your query has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse('This is the contact homepage...')
