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

        # Print to console (for debugging purposes)
        print(name, email, subject, message)

        # Success message
        messages.success(request, "Your message has been sent. Thank you!")

        # Redirect to the same page or another page
        return redirect('contact')  # Replace 'contact' with the name of your URL pattern for the contact form

    # For GET requests, render the contact form
    return render(request, 'landing.html')


def landing(request):
    return render(request, 'landing.html')
