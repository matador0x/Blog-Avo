from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("add-post", views.add_post, name="add"),
    path("post/<int:pk>/delete/", views.PostDelete.as_view(), name="post_delete"),
    path("post/<slug:slug>", views.post_details, name="post_details"),
]
