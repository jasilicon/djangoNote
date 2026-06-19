from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # Import the User model

class Note(models.Model):
    # Link the note to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('one:note_detail', kwargs={'pk': self.pk})