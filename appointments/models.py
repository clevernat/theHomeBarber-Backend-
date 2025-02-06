from django.db import models
import uuid
# Create your models here.


class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('haircut', 'Classic Haircut'),
        ('shave', 'Shave & Trim'),
        ('beard', 'Beard Styling'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f"{self.name} - {self.get_service_display()} on {self.date} at {self.time}"
