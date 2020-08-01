from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.UserCreate.as_view()),
    path('Products/', views.Product.as_view()),
    path('hello_world/', views.hello_world),
]