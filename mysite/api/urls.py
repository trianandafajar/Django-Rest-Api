from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path(
        "blogposts/<int:pk>/",
        views.BlogPostRetrieveUpdateDestroy.as_view(),  # Perbaikan typo
        name="update",
    ),
    path("blogposts/delete-all/", views.BlogPostDeleteAll.as_view(), name="delete-all"),  # Tambahkan endpoint penghapusan semua post
]
