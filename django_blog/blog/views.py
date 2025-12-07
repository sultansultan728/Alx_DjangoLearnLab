from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from .models import Comment, Post
from .forms import CommentForm
from django.urls import reverse
from django.views.generic import CreateView


# Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view using built-in Django view, we’ll use the template only
# Logout handled by built-in view

# Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

def form_valid(self, form):
        # set the logged-in user as author before saving
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post-detail", pk=post_id)
    else:
        form = CommentForm()

    return redirect("post-detail", pk=post_id)
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ["content"]
    template_name = "blog/comment_form.html"

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.id})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

# Delete Comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.id})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs["post_id"])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.kwargs["post_id"]})

