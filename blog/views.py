from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View


from .models import Post
from .forms import CommentForm
# Create your views here.


class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]        #can order it by multiple fields in the same list.
    context_object_name = "posts"
    # to query the complete data
    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data


class PostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]
    
    

class PostDetailView(View):
    def is_stored_later(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_save_for_later = post_id in stored_posts
        else:
            is_save_for_later = False
        return is_save_for_later
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(), 
            "comments": post.comments.all(), 
            "save_for_later": self.is_stored_later(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post 
            comment.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        
        context = {
            "post": post,
            "post_tags": post.tags.all(), 
            "comment_form": comment_form,
            "comments": post.comments.all(),
            "save_for_later": self.is_stored_later(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_post = request.session.get("stored_posts")
        context = {}
        if stored_post is None or len(stored_post) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in= stored_post)      #id__in is the modifier which will check if the posts are there in the stored post or not.            
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_post = request.session.get("stored_posts")

        if stored_post is None:
            stored_post = []
        
        post_id = int(request.POST["post_id"])
        if post_id not in stored_post:
            stored_post.append(post_id)
        else:
            stored_post.remove(post_id)
            
        request.session["stored_posts"] = stored_post        # to store the session data for all the posts.

        return HttpResponseRedirect("/")