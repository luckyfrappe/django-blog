from django.shortcuts import render
from .models import About

def about_detail(request):

    about_content = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about_detail.html",
        {"about_content": about_content},
    )