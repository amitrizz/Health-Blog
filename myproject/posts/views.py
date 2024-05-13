from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Post,Comments
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def post_list(request):
    if request.method == "POST":
        search_key = request.POST.get('search')
        print(search_key)
        posts = Post.objects.all().filter(title__contains=search_key)[0:10]
        return render(request, "posts/post_list.html", {"posts": posts})
    else:
      posts=Post.objects.all()    #here order by on date to sort data
    return render(request,'posts/post_list.html',{"posts":posts})

def post_page(request,slug):
    post_page = Post.objects.get(slug=slug)
    comments=Comments.objects.all().filter(post_slug=post_page).order_by('-date')
    print(comments)
    form=forms.CreateComment()
    return render(request,'posts/post_page.html',{"post_page":post_page,"form":form,"comments":comments})


@login_required(login_url="/users/login/") 
def new_comment(request):
    if request.method == "POST":
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            slug = request.POST.get('slug')
            post_page = Post.objects.get(slug=slug)
            cleaned_data = form.cleaned_data
            # Access individual form fields
            comment = cleaned_data['comment']
            print(comment)
            username = request.user.username
            comment = Comments.objects.create(
                post_slug=post_page,
                user=username,
                comment=comment
            )
            # # Save the comment to the database
            comment.save()
            return redirect('posts:post_page',slug=slug)
    else:
        return redirect("posts:list")


  

@login_required(login_url="/users/login/")   
def new_post(request):
    if request.method == "POST":
        form=forms.Createpost(request.POST,request.FILES)
        if form.is_valid():
            newpost=form.save(commit=False)
            newpost.author=request.user
            newpost.save()
            return redirect('posts:list')
    else:
       form=forms.Createpost()
    return render(request,"posts/new_post.html",{"form":form})


@login_required(login_url="/users/login/") 
def user_post(request):
    user=request.user
    alluserpost=Post.objects.all().filter(author=user)
    allusercomment=Comments.objects.all().filter(user=user)
    # username=user.username
    print(allusercomment)
    return render(request,'posts/user_post.html',{"alluserpost":alluserpost,"allusercomment":allusercomment})