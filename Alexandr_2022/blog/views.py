from django.shortcuts import render
from .models import Post, Comment, Category
from .forms import CommentForm

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comment": comments,
        "form": form
    }

    return render(request, "blog_detail.html", context)

def blog_category(request, category):
    post = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    context = {
        'post': post,
        'category': category
    }
    return render(request, "blog_category.html", context)