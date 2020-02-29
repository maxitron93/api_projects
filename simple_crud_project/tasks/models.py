from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    finished = models.BooleanField(default=False)
    finished_at_test = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
