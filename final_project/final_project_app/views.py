from lib2to3.fixes.fix_input import context

from django.http import HttpResponseServerError
from django.shortcuts import render
from django.http import HttpResponseServerError
from django.urls import path


# Create your views here.

def Handle500(request, exception = None):
    return render(request, "Handle/Error500.html", status = 500)

def index_page(request):
    context = {}
    return render(request, "general/index.html", context)

def log_in_page(request):
    context = {}
    return render(request, "auth/log_in.html", context)

def sign_up_page(request):
    context = {}
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



