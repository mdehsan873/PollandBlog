from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .form import BlogForm
from .models import Blog


def index(request):
    data = Blog.objects.all()
    blogs = {'blogs': data}
    print(blogs.values())
    return render(request, 'polls/blog_index.html', blogs)


def add(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        print(form.is_valid())
        print('Post mathod')
        if form.is_valid():
            try:
                form.save()

                return redirect('/blog')
            except Exception as e:
                print(e)
                pass
    else:
        form = BlogForm()
    return render(request, 'polls/add_blog.html', {'form': form})


def read(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/blog_read.html', {'blog': blog})
