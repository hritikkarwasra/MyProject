from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path("create_blog/", views.create_blog, name = "create_blog"),
    path('<uuid:blog_id>', views.blog_detail, name='blog_detail'),
    path('save_comment/', views.save_comment, name= 'save_comment')
]