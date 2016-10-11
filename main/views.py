from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from main.forms import ContactUs
from main.models import News, Contact


def home(request):
    contact_us_form = ContactUs(request.POST or None, auto_id=False)
    all_news = News.objects.all()
    return render(request, 'index.html', {'form': contact_us_form, 'all_news': all_news})


def exposure(request):
    return render(request, 'exposure.html')


def core(request):
    return render(request, 'core.html')


def wm(request):
    return render(request, 'wm.html')


def approval(request):
    return render(request, 'approval.html')


@csrf_exempt
def contact(request):
    form = ContactUs(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            phone = request.POST["phone_number"]
            company = request.POST["company"]
            message = request.POST["comment"]
            new_contact = Contact.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, company=company, comment=message)
            send_mail('New reservation',
                      "Message: " + message + "<br>" + "Phone: " + phone + "<br>" + "Company: " + company + "<br>" + "Email: " + email + "<br>" + "Name: " + first_name + " " + last_name,
                      "hayitsnotforanyone@gmail.com",
                      ['m.zuby@metabanks.com'], fail_silently=False,
                      html_message="Message: " + message + "<br>" + "Phone: " + phone + "<br>" + "Company: " + company + "<br>" + "Email: " + email + "<br>" + "Name: " + first_name + last_name)
            form = ContactUs()
            return render(request, 'index.html', {"form": form})
        else:
            return render(request, 'index.html', {"form": form})
    else:
        form = ContactUs()
        return render(request, 'index.html', {"form": form})