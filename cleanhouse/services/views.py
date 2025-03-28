from django.shortcuts import render
from .models import CleaningRequest

# View to display all cleaning requests
def request_list(request):
    requests = CleaningRequest.objects.all()
    return render(request, 'services/request_list.html', {'requests': requests})
