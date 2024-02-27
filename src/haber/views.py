from django.shortcuts import render
from .models import BlogModel



def blog(request):

    blogs = BlogModel.objects.all().order_by('-id')
    pagetitle = 'haberler'
    context = {
        'blogs':blogs,
        'pagetitle':pagetitle,   
    }
    return render(request, 'blog.html', context)

    