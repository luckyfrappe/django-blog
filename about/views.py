from django.shortcuts import render
from .models import About
from .forms import CollaborateRequestForm
from django.contrib import messages

def about_detail(request):

    about_content = About.objects.all().order_by("-updated_on").first()

    if request.method == "POST":
        print("Recieved a POST request")
        collaboration_form = CollaborateRequestForm(data=request.POST)
        if collaboration_form.is_valid():
            collaboration_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Request submitted, we will get in touch shortly'
            )
    collaboration_form = CollaborateRequestForm()

    return render(
        request,
        "about/about_detail.html",
        {"about_content": about_content,
         "collaboration_form": collaboration_form,},
    )

 