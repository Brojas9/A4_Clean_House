from django.shortcuts import render, redirect
from .models import CleaningRequest
from .forms import CleaningRequestForm

# View to display all cleaning requests
def request_list(request):
    requests = CleaningRequest.objects.all()
    return render(request, 'services/request_list.html', {'requests': requests})

# View to handle the form for creating a new request
def request_create(request):
    if request.method == 'POST':
        form = CleaningRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')  # Redirect after submission
    else:
        form = CleaningRequestForm()

    return render(request, 'services/request_form.html', {'form': form})