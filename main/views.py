from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.decorators.csrf import csrf_exempt

def home(request):
    posts = Post.objects.all()
    return render(request, 'main/home.html', {'posts': posts})

@csrf_exempt
@login_required
def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        if title and content:
            new_post = Post.objects.create(author=request.user, title=title, content=content)
            return JsonResponse({"status": "success", "id": new_post.id, "title": new_post.title})
        else:
            return JsonResponse({"status": "error"})

@csrf_exempt
@login_required
def delete_post(request):
    if request.method == "POST":
        post_id = request.POST.get("id")
        try:
            post = Post.objects.get(id=post_id, author=request.user)
            post.delete()
            return JsonResponse({"status": "success"})
        except Post.DoesNotExist:
            return JsonResponse({"status": "error"})

@csrf_exempt
@login_required
def edit_post(request):
    if request.method == "POST":
        post_id = request.POST.get("id")
        new_title = request.POST.get("title")
        
        try:
            post = Post.objects.get(id=post_id, author=request.user)
            post.title = new_title
            post.save()
            return JsonResponse({"status": "success"})
        except Post.DoesNotExist:
            return JsonResponse({"status": "error"})
