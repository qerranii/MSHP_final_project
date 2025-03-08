from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from final_project_app.models import Info, Comment, Post, LikePost, LikeComment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index_page(request):
    context = {}
    return render(request, "general/index.html", context)

def log_in_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/profile")
        else:
            context['error'] = "Invalid username or password"
            print('1')

    return render(request, "auth/log_in.html", context)

def sign_up_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        height = request.POST['height']
        weight = request.POST['weight']
        chest = request.POST['chest']
        waist = request.POST['waist']
        hips = request.POST['hips']
        gender = request.POST['gender']
        about_me = request.POST['about']
        if password == password2:
            try:
                user = User.objects.create_user(username, email, password)
                info = Info(user=user, height=int(height), weight=int(weight),
                            chest=int(chest), waist=int(waist), hips=int(hips), gender=int(gender), about_me=about_me)
                user.save()
                info.save()
                logout(request)
                return redirect('/log_in')
            except:
                raise NotImplementedError
        else:
            raise NotImplementedError
    return render(request, "auth/sign_up.html", context)


@login_required
def profile_page(request):
    context = {}
    context['info'] = Info.objects.get(user=request.user)
    return render(request, "profile/profile.html", context)

@login_required
def profile_edit_page(request):
    context = {}
    context['info'] = Info.objects.get(user=request.user)
    user = request.user
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        try:
            if request.POST['password1'] == request.POST['password2']:
                user.set_password(request.POST['password1'])
            user.save()
            info = Info.objects.get(user=user)
            info.height = int(request.POST['height'])
            info.weight = int(request.POST['weight'])
            info.chest = int(request.POST['chest'])
            info.waist = int(request.POST['waist'])
            info.hips = int(request.POST['hips'])
            info.gender = int(request.POST['gender'])
            info.about_me = request.POST['about']
            info.save()
            login(request, user)
            return redirect('/profile')
        except:
            raise SystemError

    return render(request, "profile/profile_edit.html", context)

@login_required
def post_page(request, id=0):
    print(id)
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        comment = Comment(user=request.user, content=request.POST['text'], post=post)
        comment.save()
    context = {
        'id':id,
        'author':post.user,
        'title':post.title,
        'description':post.description,
        'image':post.image,
        'likes':len(LikePost.objects.filter(post=post)),
        'comments':Comment.objects.filter(post=post),
    }
    return render(request, "outfits/post.html", context)

@login_required
def create_post_page(request):
    context = {}
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['description']
       # image = request.POST['image'] #?????????
        if title.isalnum() and text.isalnum():
            post = Post(user=request.user, title=title, description=text)
            post.save()
            return redirect('/post/{}'.format(post.id))
    return render(request, 'outfits/make_post.html', context)

@login_required
def send_like_post(request, id):
    context = {}
    like = LikePost.objects.filter(user=request.user, post=Post.objects.get(id=id))
    if len(like) == 0:
        like = LikePost(user=request.user, post=Post.objects.get(id=id))
        like.save()
    return redirect('/post/'+str(id))

@login_required
def catalog_page(request):
    context = {}
    # context['items'] = Items.objects.all
    return render(request, 'outfits/catalog.html', context)

def gallery_liked_page(request):
    context = {}
    return render(request, "profile/gallery_liked.html", context)

def top_outfits_page(request):
    context = {}
    return render(request, "outfits/top_outfits.html", context)

def scrolling_page(request):
    context = {}
    return render(request, "outfits/scrolling.html", context)

def about_page(request):
    context = {}
    return render(request, "info/about.html", context)

def terms_page(request):
    context = {}
    return render(request, "general/terms.html", context)



