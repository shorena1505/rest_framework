from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published = models.DateTimeField()

    def __str__(self):
        return self.title