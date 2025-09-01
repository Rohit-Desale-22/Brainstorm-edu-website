from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login



def home(request):
    return render(request, 'users/home.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        # Save user in database
        user = User.objects.create_user(username=username, email=email, password=password)
        group, created = Group.objects.get_or_create(name=role)
        user.groups.add(group)

        return redirect("login")  # go to login after signup
    return render(request, "users/signup.html")

def login_view(request):
    if request.method == "POST":
        email_from_form = request.POST["email"]
        password_from_form = request.POST["password"]

        try:
            user_object = User.objects.get(email=email_from_form)
            username_to_auth = user_object.username
        except User.DoesNotExist:
            return render(request, "users/login.html", {"error": "Invalid credentials"})

        user = authenticate(request, username=username_to_auth, password=password_from_form)

        if user is not None:
            login(request, user)

            # check role
            if user.groups.filter(name='student').exists():
                return redirect("student_dashboard")
            elif user.groups.filter(name='teacher').exists():
                return redirect("teacher_dashboard")
        else:
            # invalid login
            return render(request, "users/login.html", {"error": "Invalid credentials"})

    return render(request, "users/login.html")
