#sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.
def emailView(request):
    if request.method=='GET':
        form=ContactForm()
    else:
        form=ContactForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            from_email=form.cleaned_data['from_email']
            message=form.cleaned_data['message']

            recipients=['parbatibudhathoki3@gmail.com']

            try:
                send_mail(subject,from_email+" send "+ message,from_email,recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html",{'form':form})

def successView(request):
    return HttpResponse("success! Thank you for your message.")