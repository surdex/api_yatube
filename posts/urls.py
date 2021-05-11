from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='Post')
router.register(r'posts/(?P<id>\d+)/comments', CommentViewSet,
                basename='Comment')

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token),
    path('v1/', include(router.urls)),
]
