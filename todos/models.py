from django.db import models
from django.urls import reverse

from django.conf import settings
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    # Define CharField Choices in nested tuples with Python Constants as labels
    LOW = "L"
    MEDIUM = "M"
    HIGH = "H"
    PRIORITY_CHOICES = (
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    )

    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=LOW)
    title = models.CharField(max_length=200)
    body = models.TextField()
    # auto_now_add=True sets the model to the time when it is created
    created = models.DateField(default=timezone.now())
    # auto_now=True sets the time wheneve the model is updated
    due = models.DateField()
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class Note(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.note[:30]
