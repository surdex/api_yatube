from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Post
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def partial_update(self, request, pk):
        post = self.get_object()
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(post, data=request.data,
                                         partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        post = self.get_object()
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(post)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('id'))
        queryset = post.comments.all()
        return queryset

    def partial_update(self, request, id, pk):
        comment = self.get_object()
        if comment.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(comment, data=request.data,
                                         partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id, pk):
        comment = self.get_object()
        if comment.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(comment)
        return Response(status=status.HTTP_204_NO_CONTENT)
