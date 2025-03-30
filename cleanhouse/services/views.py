from django.shortcuts import render, redirect
from .models import CleaningRequest
from .forms import CleaningRequestForm
from django.shortcuts import get_object_or_404

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

