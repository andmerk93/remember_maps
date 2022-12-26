from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm, PostForm
from .models import Post


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'


@login_required
def index(request):
    context = {
        'posts': Post.objects.filter(author=request.user),
    }
    return render(request, 'index.html', context)


@login_required
def add_post(request):
    form = PostForm(
        request.POST or None,
    )
    if not form.is_valid():
        return render(request, 'add_post.html', {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    splitted = str(post.point).split(';')
    post.lonlatstr = f'{splitted[1]},{splitted[0]}'
    post.save()
    return redirect('index')


def page_not_found(request, exception):
    return render(request, '404.html', {'path': request.path}, status=404)
