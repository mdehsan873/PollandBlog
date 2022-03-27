from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')
def login(request):
    if request.method == "POST":
        form = (request.POST)
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