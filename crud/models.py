from django.db import models

# Create your models here.

class NoteModel(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title