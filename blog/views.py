from django.shortcuts import render

# Create your views here.

# Added following minimal view
def post_list(request):
    return render(request, 'blog/post_list.html', {}) # render (put together) our template blog/post_list.html
