from django.contrib import admin  # Import Django's admin module
from .models import CleaningRequest  # Import your model

# Register the CleaningRequest model so it appears in the admin interface
@admin.register(CleaningRequest)
class CleaningRequestAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('customer_name', 'service_date', 'email', 'created_at')

    # Add filtering by date
    list_filter = ('service_date', 'created_at')

    # Add search functionality by name and email
    search_fields = ('customer_name', 'email')
