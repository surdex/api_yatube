from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet, basename='Post')
v1_router.register(r'posts/(?P<id>\d+)/comments', CommentViewSet,
                   basename='Comment')

api_patterns = [
    path('v1/api-token-auth/', obtain_auth_token),
    path('v1/', include(v1_router.urls))
]

urlpatterns = [
    path('api/', include(api_patterns)),
]
