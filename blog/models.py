from datetime import timezone

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title