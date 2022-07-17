import hello.views
from django.urls import path, include

from django.contrib import admin

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("posts/<id>", hello.views.viewPosts, name="view_posts"),
    path("admin/", hello.views.login, name="login"),
    path("admin/user", hello.views.user, name="user"),
    path("admin/user/create", hello.views.createUser, name="create_user"),
    path("admin/user/delete/<id>", hello.views.deleteUser, name="delete_user"),
    path("admin/user/edit/<id>", hello.views.editUser, name="edit_user"),
    path("admin/posts", hello.views.posts, name="posts"),
    path("admin/posts/create", hello.views.createPosts, name="create_posts"),
    path("admin/posts/delete/<id>", hello.views.deletePosts, name="delete_posts"),
    path("admin/posts/edit/<id>", hello.views.editPosts, name="edit_posts"),
    path("admin/comments", hello.views.comments, name="comments"), 
    path("admin/comments/edit/<id>", hello.views.editComments, name="edit_comments"),
    path("admin/comments/hide/<id>", hello.views.hideComments, name="hide_comments"),
    path("admin/comments/reveal/<id>", hello.views.revealComments, name="reveal_comments"),
    path("admin/comments/delete/<id>", hello.views.deleteComments, name="delete_comments"),
    path("admin/logout", hello.views.logout, name="logout")
]