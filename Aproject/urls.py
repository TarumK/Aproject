from django.contrib import admin
from django.urls import path
from Aapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('like/<int:id>/', views.like, name='like'),
    path('dislike/<int:id>/', views.dislike, name='dislike'),

]
