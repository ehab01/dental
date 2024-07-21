from django.urls import path
from .views import CreatePostView, ListPostsView
app_name = "learning_api"
urlpatterns = [
    path('posts/', ListPostsView.as_view(), name='list_posts'),
    path('posts/create/', CreatePostView.as_view(), name='create_post'),
]