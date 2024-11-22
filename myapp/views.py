from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data (you can save it or use it as needed)
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            
            # Example: storing data in the session (you can store in a database)
            request.session['name'] = name
            request.session['gender'] = gender
            request.session['email'] = email
            request.session['city'] = city
            
            messages.success(request, "Registration successful!")
            return render(request, 'myapp/register.html', {'form': form})
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()

    return render(request, 'myapp/register.html', {'form': form})
