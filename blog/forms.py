from django import forms
from .models import Post, Comment


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body", "overview", "image")


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")
