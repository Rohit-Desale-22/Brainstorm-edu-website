from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def student_dashboard(request):
    return render(request, 'dashboard/student_dashboard.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'dashboard/teacher_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect("login")
