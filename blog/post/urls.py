from django.urls import path
from . import views
urlpatterns = [
    path('posts/<int:post_pk>/comments/', views.comment_list, name='comment-list'),
    path('posts/', views.PostListView,name='Posts'),
    path('posts/<int:pk>/',views.PostDetailView,name='Post'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/update/<int:pk>/', views.update_post, name='update_post'),
     path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),

   
]
