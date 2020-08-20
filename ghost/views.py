from django.shortcuts import render, HttpResponseRedirect, reverse

from ghost.models import Post
from ghost.forms import CreatePostForm

def index_view(request):
    my_posts = Post.objects.order_by('-date_time')
    return render(request, "index.html", {"posts": my_posts})

def boast_view(request):
    my_posts = Post.objects.filter(is_boast=True).order_by('-date_time')
    return render(request, "index.html", {"posts": my_posts})

def roast_view(request):
    my_posts = Post.objects.filter(is_boast=False).order_by('-date_time')
    return render(request, "index.html", {"posts": my_posts})

def score_view(request):
    my_posts = Post.objects.order_by('-score')
    return render(request, "index.html", {"posts": my_posts})
    

def create_post_view(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                text=data.get('text'),
                is_boast=data.get('boast_or_roast'),
            )
            return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
    form = CreatePostForm
    return render(request, "create_post_form.html", {"form":form})

def up_vote_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.score += 1
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def down_vote_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.score -= 1
    post.down_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))
    
