from django.shortcuts import render , HttpResponse
from datetime import datetime
from App1.models import Contact
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable" : "Joe Mama",
        "variable2": "Is Hawt"
    }
    return render(request, 'index.html', context)
   # return HttpResponse("This is homepage")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request , 'services.html')
    # return HttpResponse("This is services page")

@csrf_exempt   
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name , email=email , phone = phone , desc = desc , date = datetime.today())
        contact.save();
        messages.success(request, 'Contact Info saved successfully!')
    return render(request , 'contact.html')
    # return HttpResponse("This is contact page")