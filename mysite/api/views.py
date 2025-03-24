from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListCreate(generics.ListCreateAPIView):
    """
    API View untuk menampilkan daftar blog post dan membuat post baru.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API View untuk mengambil, memperbarui, atau menghapus blog post berdasarkan primary key (pk).
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


class BlogPostDeleteAll(generics.DestroyAPIView):
    """
    API View untuk menghapus semua blog post.
    """
    queryset = BlogPost.objects.all()

    def delete(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return Response({"message": "All blog posts deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
