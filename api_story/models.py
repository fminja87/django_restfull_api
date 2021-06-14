from django.db import models


# Create your models here.


class Story(models.Model):
    story_title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.story_title
