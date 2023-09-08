from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404, HttpRequest, HttpResponse
from braces.views import SelectRelatedMixin
from django.contrib import messages
from . import forms
from django.core.exceptions import ObjectDoesNotExist
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from posts.models import Post,Comment
from posts.forms import CommentForm

from django.shortcuts import redirect

from django.contrib.auth import get_user_model
User = get_user_model()

class PostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    select_related = ('user','group') #What the post belong to

class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:  # Change ValueError to User.DoesNotExist
            raise Http404
        else:
            return self.post_user.posts.all()
        
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group') 

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):

    fields = ('message','group')
    model = models.Post

    def form_valid(self,form):
        print(dir(self))
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        print("test")
        return super().form_valid(form)
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
    

    
class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all') # redirect to all the posts

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
    
class PostDetailView(generic.DetailView):
    model = Post
    select_related = ('user','group')


def postList(request):
    return render(request, 'posts/post_list.html')


class postAll(TemplateView):
    template_name = 'posts/post_all.html'


def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk) #Get post object
    if request.method == 'POST':
        form = CommentForm(request.POST) #Pass in the request
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts:allPost')
    else:
        form = CommentForm()
    return render(request,'posts/comment_form.html',{'form':form})