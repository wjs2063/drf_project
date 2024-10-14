from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('blog', include('blog.urls')),
]


