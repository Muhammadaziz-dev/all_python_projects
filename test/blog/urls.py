from .views import blog_list_view, detailview
from django.urls import path

urlpatterns = [
    path("", blog_list_view, name="blog_list_view"),
    path("blogs/<int:id>/", detailview, name="blog_detail"),
]