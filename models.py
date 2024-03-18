from django.db import models

class Reminder(models.Model):
    time = models.DateTimeField()
    message = models.TextField()
    method = models.CharField(max_length=10)
