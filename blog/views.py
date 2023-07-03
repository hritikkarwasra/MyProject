from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import Blogs, Comments

# Create your views here.

def index(request):
    blogs = Blogs.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request, 'blog/blog.html', context)

def create_blog(request):
    message= "Failed Creation"
    status = 400
    try:
        if request.method == "POST":
            print("hi")
            title = request.POST.get("blog_title")
            author_name = request.POST.get("author_name")
            content = request.POST.get("content")
            publication_date = request.POST.get("publicationDate")

            blog = Blogs(title = title, author_name = author_name, content = content, publication_date= publication_date)
            blog.save()

            message = "successfully created"
            status = 200
    except Exception as e:
        print(e)

    return HttpResponse(message , status)

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id)
    blog_comments = Comments.objects.filter(blog = blog).all()
    context = {
        'blog': blog,
        'blog_comments': blog_comments
    }
    print("here")
    return render(request, 'blog/blog_detail.html', context)

def save_comment(request):
    message= "Failed Creation"
    status = 400
    try:
        if request.method == "POST":
            print("hi")
            blog_id = request.POST.get("blog_id")
            comment_text = request.POST.get("comment_text")
            blog_obj = Blogs.objects.filter(id = blog_id).first()
            comment_obj = Comments(comment= comment_text, blog = blog_obj)
            comment_obj.save()
            print(comment_text,blog_id)

            message = "successfully created"
            status = 200
    except Exception as e:
        print(e)

    return HttpResponse(message , status)