from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blogpost
# Create your views here.
def index(request):
    data=Blogpost.objects.all()
    print(data)
    # to display all the posts
    return render(request,'blog/index.html',{'post':data})

def blogpost(request,id):
    # to display the post content to blogpost page based on id    
    post=Blogpost.objects.filter(post_id=id)[0]
    
    return render(request,'blog/blogpost.html',{'post':post})
