from django.urls import path 
from . import views 

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name="post-list"),
    path('new/', views.CreatePost.as_view(), name='create-post'),
    path('edit/<slug:slug>', views.EditPost.as_view(), name='edit-post'),
    path('remove/<slug:slug>', views.RemovePost.as_view(), name='remove-post'),
    path('view/<slug:slug>', views.ViewPost.as_view(), name='view-post'),
    path('tag/<str:tag>', views.tagged_posts, name='tag'),
]
