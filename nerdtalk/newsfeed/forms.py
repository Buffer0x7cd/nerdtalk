from django import forms
from newsfeed.models import Post

class PostForm(forms.ModelForm):
    ''' Form class for new submission '''
    class Meta:
        model = Post
        fields = ('title', 'content')

