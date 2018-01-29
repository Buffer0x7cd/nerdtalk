from django.db import models
from django.utils import timezone


class Post(models.Model):
    '''Post a content '''
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length= 256)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    upvote = models.IntegerField(default=1)


    def __str__(self):
        return self.title

