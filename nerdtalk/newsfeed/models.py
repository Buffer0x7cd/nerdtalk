from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.shortcuts import reverse

class Post(models.Model):
    '''Post a content '''
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length= 256)
    content = HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    upvote = models.ManyToManyField('auth.User', related_name='voters')


    def __str__(self):
        return self.title

    def is_owner(self, user):
        return self.author == user

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})