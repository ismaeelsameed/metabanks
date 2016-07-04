from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from main.forms import ContactUs
from main.models import News, Contact


def home(request):
    contact_us_form = ContactUs(request.POST or None, auto_id=False)
    all_news = News.objects.all()
    return render(request, 'index.html', {'form': contact_us_form, 'all_news': all_news})


def products(request):
    return render(request, 'products.html')


@csrf_exempt
def contact(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["phone_number"]
        message = request.POST["comment"]
        new_contact = Contact.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, comment=message)
        # send_mail('New reservation',
        #           "Message: " + message + "<br>" + "Phone: " + phone + "<br>" + "Email: " + email + "<br>" + "Name: " + first_name + last_name,
        #           "distinctshots@gmail.com",
        #           ['distinctshots@gmail.com'], fail_silently=False,
        #           html_message="Message: " + message + "<br>" + "Phone: " + phone + "<br>" + "Email: " + email + "<br>" + "Name: " + first_name + last_name)
    return HttpResponse("done")
