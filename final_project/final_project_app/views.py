from django.shortcuts import render, redirect
from final_project_app.models import Info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def index_page(request):
    context = {}
    return render(request, "profile/profile.html", context)

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
        about_me = request.POST['about']
        if password == password2:
            try:
                user = User.objects.create_user(username, email, password)
                info = Info(user=user, height=int(height), weight=int(weight),
                            chest=int(chest), waist=int(waist), hips=int(hips), about_me=about_me)
                user.save()
                info.save()
                return redirect('/profile')
            except:
                raise NotImplementedError
        else:
            raise NotImplementedError
    return render(request, "auth/sign_up.html", context)

def profile_page(request):
    context = {}
    return render(request, "profile/profile.html", context)

def profile_edit_page(request):
    context = {}
    return render(request, "profile/profile_edit.html", context)

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



