from django.shortcuts import render

# Create your views here.
def articles(request):
    return render(request,'blog/blog.html')