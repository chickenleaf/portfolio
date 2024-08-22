from django.shortcuts import render, redirect
from website.models import Contact  
from django.contrib import messages

# Create your views here.



def contact_view(request):
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        print(name, email, subject, message)

        # Success message
        messages.success(request, "Your message has been sent. Thank you!")
        

        # Redirect to the same page to avoid form resubmission
        return render(request, 'landing.html')


def landing(request):
    return render(request, 'landing.html')
