from django.shortcuts import render, redirect
from final_project_app.models import User
# Create your views here.

def index_page(request):
    context = {}
    return render(request, "general/index.html", context)

def log_in_page(request):
    context = {}
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
        if password == password2:
            user = User.objects.create_user(username, email, password, height, weight, chest, waist, hips)
            try:
                user.save()
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



