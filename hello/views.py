from os import execv
import re
from urllib.robotparser import RobotFileParser
from django.shortcuts import redirect, render
from django.db.models import Avg

from .models import Posts, User, Comments, Ratings

# Create your views here.

def logout(request):
    del request.session['role']
    del request.session['username']
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def index(request):
    return render(request, "index.html", {"username": request.session.get('username'), "posts": Posts.objects.all()[::-1], "most_read": Posts.objects.order_by("-views")})


def viewPosts(request, id):
    comments_raw = Comments.objects.filter(hidden = False, post_id = id)[::-1]

    """---render ratings---"""
    try:
        ratings = Ratings.objects.get(post_id = id, author_id = request.session.get("author_id"))
    except:
        ratings = None

    try:
        average_rating = round(list(Ratings.objects.filter(post_id = id).aggregate(Avg('rating')).values())[0], 1)
    except:
        average_rating = None

    if request.method == "POST":
        """---create comment---"""
        if "create_comment" in request.POST and len(request.POST.get("detail")) > 31:
            comments = Comments()
            comments.detail = request.POST.get("detail")
            comments.author_id = request.session.get("author_id")
            comments.post_id = id
            comments.save()

        # """---ratings---"""
        elif "ratings_form" in request.POST:
            if not ratings:
                ratings = Ratings()
                ratings.post_id = id
                ratings.author_id = request.session.get("author_id")
                ratings.rating = request.POST.get("rating-input")
                ratings.save()
            else:
                ratings.rating = request.POST.get("rating-input")
                ratings.save()

        return redirect(request.META['HTTP_REFERER'])

    """---process comments---"""
    comments = []
    for comment_raw in comments_raw:
        user = User.objects.get(id = comment_raw.author_id)
        comment = {
            "id": comment_raw.id,
            "detail": comment_raw.detail,
            "updated_at": comment_raw.updated_at,
            "author_name": user.name,
        }
        comments.append(comment)

    """---count views---"""
    post = Posts.objects.get(pk = id)
    post.views += 1
    post.save()

    return render(request, "view_post.html", {
        "comments": comments, 
        "ratings": ratings,
        "average_rating": average_rating,
        "username": request.session.get('username'), 
        "posts": post, 
        "role": request.session.get('role'),
        }
    )


def login(request):
    role = request.session.get('role')
    if role:
        if role == '0' or role == '1':
            return redirect("/admin/user")
        else:
            return redirect("/admin/posts")

    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            try:
                user = User.objects.get(username = username)
                if password == user.password:
                    request.session['username'] = username
                    if int(user.role) == 0:
                        request.session['role'] = '0'
                    elif int(user.role) == 1:
                        request.session['role'] = '1'
                    else:
                        request.session['role'] = '2'
                    return redirect(request.POST.get('next', '/'))
            except User.DoesNotExist:
                return redirect("/admin")
            return redirect("/admin")

        elif "register_form" in request.POST:
            user = User()
            user.name = request.POST.get("name")
            user.username = request.POST.get("username")
            user.password = request.POST.get("password")
            user.role = 2
            user.save()
            return redirect("/admin")
    return render(request, "admin_login.html")


"""---user views---"""


def user(request):
    role = request.session.get('role')

    if role == '0' or role == '1':
        return render(request, "admin_user.html", {"user": User.objects.all(), "role": role, "username": request.session.get('username')})
    return redirect("/admin/posts")


def createUser(request):
    role = request.session.get('role')
    if request.method == "POST":
        user = User()
        user.name = request.POST.get("name")
        user.username = request.POST.get("username")
        user.password = request.POST.get("password")
        if role == 1:
            user.role = int(request.POST.get("role"))
        else:
            user.role = 2
        user.save()
        return redirect("/admin/user")

    if role == '0' or role == '1':
        return render(request, "admin_user_create.html", {"role": role})
    return redirect("/admin/posts")


def deleteUser(request, id):
    role = request.session.get('role')
    if role == '0' or user.role == 2:
        User.objects.get(pk = id).delete()
        return redirect(request.META['HTTP_REFERER'])
    return redirect("/admin/posts")


def editUser(request, id):
    role = request.session.get('role')
    user = User.objects.get(pk = id)
    if request.method == "POST":
        user.name = request.POST.get("name")
        user.username = request.POST.get("username")
        user.password = request.POST.get("password")
        if int(request.POST.get("role")) == 1:
            user.role = int(request.POST.get("role"))
        else:
            user.role = 2
        user.save()
        return redirect("/admin/user")

    if role == '0':
        return render(request, "admin_user_edit.html", {"user": user, "role": RobotFileParser})
    return redirect("/admin/posts")


"""---posts views---"""


def posts(request):
    role = request.session.get('role')

    if role == '0' or role == '1':
        return render(request, "admin_posts.html", {"posts": Posts.objects.all()[::-1], "role": role})
    elif role == '2':
        return render(request, "admin_posts.html", {"posts": Posts.objects.filter(author=request.session.get('username')), "role": role})
    return redirect("/admin")


def createPosts(request):
    username = request.session.get('username')
    if request.method == "POST":
        posts = Posts()
        posts.title = request.POST.get("title")
        posts.img = request.POST.get("title")
        posts.description = request.POST.get("description")
        posts.detail = request.POST.get("detail")
        posts.author = username
        posts.save()
        return redirect("/admin/posts")

    if 'role' in request.session:
        return render(request, "admin_posts_create.html", {"role": request.session.get('role')})
    return redirect("/admin")


def deletePosts(request, id):
    role = request.session.get('role')
    username = request.session.get('username')
    posts = Posts.objects.get(pk = id)
    if role == '0' or role == '1' or posts.author == username:
        posts.delete()
        return redirect(request.META['HTTP_REFERER'])
    return redirect("/admin")


def editPosts(request, id):
    role = request.session.get('role')
    username = request.session.get('username')
    posts = Posts.objects.get(pk = id)
    if request.method == "POST":
        posts.title = request.POST.get("title")
        posts.img = request.POST.get("title")
        posts.description = request.POST.get("description")
        posts.detail = request.POST.get("detail")
        posts.save()
        return redirect("/admin/posts")

    if role == '0' or role == '1' or username == posts.author:
        return render(request, "admin_posts_edit.html", {"posts": posts, "role": role})
    return redirect("/admin")


"""---comments views---"""

def comments(request):
    comments_raw = Comments.objects.all().order_by('-updated_at')
    role = request.session.get('role')

    comments = []
    for comment_raw in comments_raw:
        user = User.objects.get(id = comment_raw.author_id)
        post = Posts.objects.get(id = comment_raw.post_id)
        comment = {
            "id": comment_raw.id,
            "post": post.title,
            "post_id": comment_raw.post_id,
            "detail": comment_raw.detail,
            "author_name": user.name,
            "author_username": user.username,
            "updated_at": comment_raw.updated_at,
            "hidden": comment_raw.hidden,
        }
        comments.append(comment)

    if role == '0' or role == '1':
        return render(request, "admin_comments.html", {"user": User.objects.all(), "comments": comments, "role": role, "username": request.session.get('username')})
    elif role == '2':
        return render(request, "admin_comments.html", {"comments": comments.filter(author = request.session.get('username')), "role": role})
    return redirect("/admin")


def editComments(request, id):
    role = request.session.get('role')
    username = request.session.get('username')
    comments = Comments.objects.get(pk = id)
    user = User.objects.get(id = comments.author_id)
    if request.method == "POST":
        comments.detail = request.POST.get("detail")
        comments.save()
        return redirect("/admin/comments")

    if role == '0' or role == '1' or user.username == username:
        return render(request, "admin_comments_edit.html", {"comments": comments, "role": role})
    return redirect(request.META['HTTP_REFERER'])


def hideComments(request, id):
    comment = Comments.objects.get(pk = id)
    comment.hidden = True
    comment.save()
    return redirect(request.META['HTTP_REFERER'])

def revealComments(request, id):
    comment = Comments.objects.get(pk = id)
    comment.hidden = False
    comment.save()
    return redirect(request.META['HTTP_REFERER'])

def deleteComments(request, id):
    Comments.objects.get(pk = id).delete()
    return redirect(request.META['HTTP_REFERER'])