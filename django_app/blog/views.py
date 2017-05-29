from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from .models import Post

def post_list(request):
    # post 변수에 orm을 이용해서 전체 post의 리스트(쿼리셋)를 대입
    # posts = Post.objects.all()
    posts =Post.objects.filter(published_date__lte=timezone.now())
    print(posts)

    # posts published_date가 timezone.now()보다 작음 값을 가질때만
    # return HttpResponse('<html><body>Post List</body></html>')
    context={
        'title':'PostList from post_list view',
        'posts':posts,
    }

    return render(request, 'blog/post_list.html',context=context)

