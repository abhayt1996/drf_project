from django.urls import path, include
from posts.views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('api/posts/', PostListAPIView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('api-auth/', include('rest_framework.urls')),  # Add authentication URLs
]
