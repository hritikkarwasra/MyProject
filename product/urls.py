from django.urls import path, include
from product import views 

urlpatterns = [
    path('', views.index , name = 'index'),
    path('create_product/', views.create_product, name = "create_product"),
    path('create_category/', views.create_category, name = "create_category")
]