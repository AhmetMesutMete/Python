from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


# Create your views here.
def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "Username or password is wrong!"
            })
    return render(request, "account/login.html")
def register_request(request):
    return render(request, "account/register.html")

def logout_request(request):
    return render(request, "account/logout.html")