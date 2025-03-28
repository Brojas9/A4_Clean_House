from django.db import models  # Import Django's model base class

# This model represents a cleaning service request
class CleaningRequest(models.Model):
    # Customer's full name
    customer_name = models.CharField(max_length=100)

    # Address where the service is requested
    address = models.TextField()

    # Date when the customer wants the service
    service_date = models.DateField()

    # Customer's email address
    email = models.EmailField()

    # Optional notes provided by the customer
    notes = models.TextField(blank=True)

    # Automatically sets the timestamp when the request is created
    created_at = models.DateTimeField(auto_now_add=True)

    # This will define how the object shows up in the Django admin interface
    def __str__(self):
        return f"Request by {self.customer_name} on {self.service_date}"
