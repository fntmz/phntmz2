import re
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Posts, User, Comments

# Create your views here.

def logout(request):
    del request.session['role']
    del request.session['username']
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def darkmode(request):
    if not request.session.get('darkmode'):
        request.session['darkmode'] = 'dark_theme'
    else:
        if request.session.get('darkmode') == 'dark_theme':
            request.session['darkmode'] = 'light_theme'
        else:
            request.session['darkmode'] = 'dark_theme'


def index(request):
    return render(request, "index.html", {"username": request.session.get('username'), "posts": Posts.objects.all()[::-1], "darkmode": request.session.get('darkmode')})


def viewPosts(request, id):
    if request.method == "POST":
        if "create_comment" in request.POST and len(request.POST.get("detail")) > 31:
            comments = Comments()
            comments.detail = request.POST.get("detail")
            comments.author_id = request.session.get("author_id")
            comments.post_id = id
            comments.save()

        elif "edit_comment" in request.POST and len(request.POST.get("detail")) > 31:
            comments = Comments.objects.get(pk = id)
            comments.detail = request.POST.get("detail")
            comments.save()

        return redirect(request.META['HTTP_REFERER'])

    return render(request, "view_post.html", {"comments": Comments.objects.all()[::-1], "username": request.session.get('username'), "posts": Posts.objects.get(pk=id), "darkmode": request.session.get('darkmode')})


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
                    request.session['author_id'] = user.id
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
    return render(request, "admin_login.html", {"darkmode": request.session.get('darkmode')})


"""---user views---"""


def user(request):
    role = request.session.get('role')
    print(role)

    if role == '0' or role == '1':
        return render(request, "admin_user.html", {"user": User.objects.all(), "role": role, "username": request.session.get('username'), "darkmode": request.session.get('darkmode')})
    else:
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
        return render(request, "admin_user_create.html", {"role": role, "darkmode": request.session.get('darkmode')})
    else:
        return redirect("/admin/posts")


def deleteUser(request, id):
    role = request.session.get('role')
    user = User.objects.get(pk = id)
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
        return render(request, "admin_user_edit.html", {"user": user, "role": role, "darkmode": request.session.get('darkmode')})
    else:
        return redirect("/admin/posts")


"""---posts views---"""


def posts(request):
    role = request.session.get('role')

    if role == '0' or role == '1':
        return render(request, "admin_posts.html", {"posts": Posts.objects.all()[::-1], "role": role, "darkmode": request.session.get('darkmode')})
    elif role == '2':
        return render(request, "admin_posts.html", {"posts": Posts.objects.filter(author=request.session.get('username')), "role": role, "darkmode": request.session.get('darkmode')})
    else:
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
        return render(request, "admin_posts_create.html", {"role": request.session.get('role'), "darkmode": request.session.get('darkmode')})
    else:
        return redirect("/admin")


def deletePosts(request, id):
    role = request.session.get('role')
    username = request.session.get('username')
    if role == '0' or role == '1' or username == username:
        Posts.objects.get(pk = id).delete()
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

    if role == '0' or role == '1' or username == username:
        return render(request, "admin_posts_edit.html", {"posts": posts, "role": request.session.get('role'), "darkmode": request.session.get('darkmode')})
    else:
        return redirect("/admin")


"""---comments views---"""

def deleteComments(request, id):
    Comments.objects.get(pk = id).delete()
    return redirect(request.META['HTTP_REFERER'])