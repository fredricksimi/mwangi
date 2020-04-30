from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostCreateForm, PostUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Post



def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)


def post_detail(request, id):
    the_post = get_object_or_404(Post, id=id)
    context = { 'the_post':the_post}
    return render(request, 'blog/detail.html', context)



@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST or None)
        if form.is_valid():
            the_data = form.save(commit=False)
            the_data.date_posted= timezone.now()
            the_data.author = request.user
            the_data.save()
            return redirect('blog:home')
    else:
        form = PostCreateForm()
    context = {
        'form':form
    }
    return render(request, 'blog/create.html', context)



@login_required
def post_update_view(request, id):
    the_post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST or None, instance=the_post)
        if form.is_valid():
            the_update = form.save(commit=False)
            the_update.date_posted = timezone.now()
            the_update.author = request.user
            the_update.save()
            return redirect('blog:home')
    else:
        form = PostUpdateForm(instance=the_post)
    context = { 'form': form }
    return render(request, 'blog/update.html', context)



@login_required
def post_delete_view(request, id):
    the_post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        the_post.delete()
        return redirect('blog:home')
    context = {'the_post': the_post}
    return render(request, 'blog/delete.html', context)
