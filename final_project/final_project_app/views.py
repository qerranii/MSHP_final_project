from django.shortcuts import render
import requests
import json

# Create your views here.

def test_page(request):
    context = {}
    if(request.method == 'POST'):
        js = {
            "user": "name",
            "id": 4,
            "rating": 5
        }
        # Сериализуем JSON-объект в строку
        js_str = json.dumps(js)
        r = requests.get(f'http://127.0.0.1:8081/getrec?data={js_str}')
        print(r.text)
    return render(request, 'test.html', context)

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



