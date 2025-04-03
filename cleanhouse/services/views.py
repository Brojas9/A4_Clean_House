from django.shortcuts import render, redirect
from .models import CleaningRequest
from .forms import CleaningRequestForm
from django.shortcuts import get_object_or_404


ADMIN_PASSWORD = 'NetworkingA4!'  # this must match exactly

# Admin-only view to list all cleaning requests
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


def admin_login(request):
    error = None
    if request.method == 'POST':
        password = request.POST.get('password')
        print("Entered password:", password)  # ← ADD THIS
        print("Expected password:", ADMIN_PASSWORD)  # ← AND THIS

        if password == ADMIN_PASSWORD:
            request.session['is_admin'] = True
            print("Login successful!")  # ← CHECK FOR THIS MESSAGE
            return redirect('request_list_admin')
        else:
            print("Login failed.")  # ← CHECK FOR THIS MESSAGE
            error = "Incorrect password. Try again."

    return render(request, 'services/admin_login.html', {'error': error})


# View to handle the form for creating a new request
def request_create(request):
    if request.method == 'POST':
        form = CleaningRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to thank you page
    else:
        form = CleaningRequestForm()

    return render(request, 'services/request_form.html', {'form': form})

# View to handle editing a cleaning request
def request_update(request, pk):
    request_instance = get_object_or_404(CleaningRequest, pk=pk)
    if request.method == 'POST':
        form = CleaningRequestForm(request.POST, instance=request_instance)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = CleaningRequestForm(instance=request_instance)

    return render(request, 'services/request_form.html', {'form': form})

# View to handle deletion a cleaning request
def request_delete(request, pk):
    request_instance = get_object_or_404(CleaningRequest, pk=pk)
    if request.method == 'POST':
        request_instance.delete()
        return redirect('request_list')
    return render(request, 'services/request_confirm_delete.html', {'object': request_instance})

# View to handle Main Page
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
    return redirect('main_page')  # Or use 'home' depending on your URL name
