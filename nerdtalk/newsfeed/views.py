from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import login
from newsfeed.forms import PostForm
from newsfeed.models import Post
from django.contrib import messages


@login_required
def post_list(request):
    ''' Render the list of published post'''
    posts =  Post.objects.all().order_by('-created_date')
    context = {'posts':posts}
    return render(request, 'newsfeed/post_list.html', context )


def root(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        return redirect('login')



@login_required
def post_new(request):
    ''' Create a new post'''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post  = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form =  PostForm()
    return render(request, 'newsfeed/post_edit.html', {'form': form})


@login_required
def post_detail(request, pk):
    ''' Show full blog'''
    post =  get_object_or_404(Post, pk=pk)
    return render(request, 'newsfeed/post_detail.html', {'post':post})


@login_required
def post_edit(request, pk):
    ''' Edit a post'''
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'newsfeed/post_edit.html', {'form': form})



@login_required
def delete(request, pk):
    ''' Delete a post'''
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')

@login_required
def upvote(request, pk):
    ''' Upvote a post'''
    post = get_object_or_404(Post, pk=pk)
    if request.user not in post.upvote.all():
        post.upvote.add(request.user)
    else:
        messages.error(request, 'Oops, looks like you have already upvoted this post')        
    return redirect('post_detail', pk=pk)

        