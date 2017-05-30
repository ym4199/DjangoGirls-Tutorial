from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your views here.

from .forms import PostCreateForm

User=get_user_model()
from .models import Post

def post_list(request):
    # post 변수에 orm을 이용해서 전체 post의 리스트(쿼리셋)를 대입
    # posts = Post.objects.all()
    posts =Post.objects.order_by('-created_date')

    print(posts)

    # posts published_date가 timezone.now()보다 작음 값을 가질때만
    # return HttpResponse('<html><body>Post List</body></html>')
    context={
        'title':'PostList from post_list view',
        'posts':posts,
    }

    return render(request, 'blog/post_list.html',context=context)

def post_detail(request, pk):
    print('post_detail pk:',pk)
    # context 에 post라는 키값으로 pk 또는 id 값이 매개변수로 주어진 pk변수와 같은 post객체를 전달
    context={
        'post': Post.objects.get(pk=pk)
    }
    return render(request,'blog/post_detail.html',context)


def post_create(request):
    if request.method == 'GET':
        form =PostCreateForm()
        context={
            'form':form,
        }
        return render(request, 'blog/post_create.html',context)
    elif request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            # data = request.POST
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            user = User.objects.first()
            post = Post.objects.create(
                title = title,
                text = text,
                author = user,
            )
            return redirect('post_detail',pk=post.pk)
        else:
            context = {
                'form':form,
            }
        # return HttpResponse('post_create POST request')
        return redirect('post_detail')


def post_modify(request, pk):
    post=Post.objects.get(pk=pk)
    if request.method == 'POST':
        data = request.POST
        title = data['title']
        text = data['text']
        post.title = title
        post.text = text
        post.save()
        return redirect('post_detail', pk = pk)
    elif request.method == 'GET':
        context = {
            'post':post,
        }
    return render(request, 'blog/post_modify.html',context)