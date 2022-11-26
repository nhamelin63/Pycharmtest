from django.contrib import admin
from django.urls import path, include
from .views import index, detail
urlpatterns = [
    path('', index.as_view(), name='index'),
    path('<slug:slug>/', detail.as_view(), name='detail'),
]
