<<<<<<< HEAD
# Create your views here
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,
 'blog/post/list.html',
 {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post}, status=Post.Status.PUBLISHED)
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,slug=post,publish__year=year,publish__month=month,publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    
    return render(request,'blog/post/detail.html',{'post': post,'comments': comments,'form': form})
=======


# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post
def post_list(request):
        posts = Post.published.all()
        return render(request,
        'blog/post/list.html',
        {'posts': posts})
def post_detail(request, id):
        post = get_object_or_404(Post,
        id=id,
        status=Post.Status.PUBLISHED)
        return render(request,
        'blog/post/detail.html',
        {'post': post})
def post_detail(request, id):
        post = get_object_or_404(Post,
        id=id,
        status=Post.Status.PUBLISHED)
        return render(request,
        'blog/post/detail.html',
        {'post': post})
>>>>>>> 761f8fac9ce22fdea80e4ba390301800017b8f42
