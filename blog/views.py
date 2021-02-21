from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def post_list(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 4)  # Show 5 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"posts": page_obj}
    return render(request, "blog/blog.html", context)


def post_details(request, slug):
    post_detail = get_object_or_404(Post, slug=slug)
    comments = post_detail.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = AddComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post_detail
            new_comment.save()
    else:
        comment_form = AddComment(data=request.POST)

    context = {
        "post_detail": post_detail,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }
    return render(request, "blog/post_details.html", context)


@login_required()
def add_post(request):
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.author = request.user
            myForm.save()
            return redirect(reverse("blog:post_list"))
    else:
        form = AddPost()

    context = {"form": form}
    return render(request, "blog/add-post.html", context)


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/post_delete.html"
