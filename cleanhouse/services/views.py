from django.shortcuts import render, redirect
from .models import CleaningRequest
from .forms import CleaningRequestForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Password used for admin login.
ADMIN_PASSWORD = 'NetworkingA4!'

# === Admin Panel ===
# This view shows all cleaning requests, but only to admin users
def request_list_admin(request):
    if request.session.get('is_admin'):
        requests = CleaningRequest.objects.all()
        return render(request, 'services/request_list.html', {
            'requests': requests,
            'authenticated': True  
        })
    return render(request, 'services/request_list.html', {
        'authenticated': False  # Show login form
    })

# Admin login form view
def admin_login(request):
    error = None
    if request.method == 'POST':
        password = request.POST.get('password')

        if password == ADMIN_PASSWORD:
            request.session['is_admin'] = True
            return redirect('request_list_admin')
        else:
            error = "Incorrect password. Try again."

    return render(request, 'services/admin_login.html', {'error': error})

# Form to create a new cleaning request
def request_create(request):
    if request.method == 'POST':
        form = CleaningRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to thank you page
    else:
        form = CleaningRequestForm()

    return render(request, 'services/request_form.html', {'form': form})

# Form to edit an existing request
def request_update(request, pk):
    request_instance = get_object_or_404(CleaningRequest, pk=pk)
    if request.method == 'POST':
        form = CleaningRequestForm(request.POST, instance=request_instance)
        if form.is_valid():
            form.save()
            return redirect('request_list_admin')
    else:
        form = CleaningRequestForm(instance=request_instance)

    return render(request, 'services/request_form.html', {'form': form})

# Confirm and delete a cleaning request
def request_delete(request, pk):
    request_instance = get_object_or_404(CleaningRequest, pk=pk)
    if request.method == 'POST':
        customer_name = request_instance.customer_name
        request_instance.delete()
        messages.success(request, f"{customer_name} was successfully deleted!")
        return redirect('request_list_admin')
    return render(request, 'services/request_confirm_delete.html', {'object': request_instance})


# Show the main landing page
def main_page(request):
    return render(request, 'services/main_page.html')

# View to handle Back to Main Page
def home(request):
    return render(request, 'services/main_page.html')

# thank_you view
def thank_you(request):
    return render(request, 'services/thank_you.html')


# View to log out admin user
def admin_logout(request):
    request.session.pop('is_admin', None)
    return redirect('main_page')   # Go back to main page
