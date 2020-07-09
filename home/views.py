from django.shortcuts import render, HttpResponse

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
    return render(request, 'contact.html')
    # return HttpResponse('This is the contact homepage...')
