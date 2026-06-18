from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = [
        ('todo', 'TO DO'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(
        upload_to='tasks/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )

    due_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
        