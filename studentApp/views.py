
from django.shortcuts import render, redirect
from studentApp.models import Course , Student, Division 
from adminApp.models import Subject
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages



def dashboard(request):
    return render(request, 'studentApp/index.html')


def profile(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
    return render(request, 'studentApp/profile.html', {'student': student})


@login_required
def change_pass(request):
    
    if request.method == "POST":
        old_password = request.POST.get("oldPassword")
        new_password = request.POST.get("newPassword")
        confirm_password = request.POST.get("confirmPassword")

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match!")
            return redirect("change_password")

        user = request.user
        if not user.check_password(old_password):
            messages.error(request, "Old password is incorrect!")
            return redirect("change_password")

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  # Keep the user logged in after password change

        messages.success(request, "Password changed successfully!")
        return redirect("dashboard")  # Redirect to a success page or dashboard

    
    return render(request , 'studentApp/change_Pass.html')

@login_required
def update_profile(request):
    student = Student.objects.get(user=request.user)

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        guardian_name = request.POST.get("guardian_name")
        guardian_phone = request.POST.get("guardian_phone")

        # Update User model
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()

        # Update Student model
        student.phone = phone
        student.address = address
        student.guardian_name = guardian_name
        student.guardian_phone = guardian_phone

        if "profile_picture" in request.FILES:
            student.profile_picture = request.FILES["profile_picture"]

        student.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("update_profile")  # Redirect to the profile page after update

    return render(request, "studentApp/profile.html", {"student": student})

def view_subjects(request):
    if request.user.is_authenticated:
        try:
            # Attempt to get the user's existing cart
            student = Student.objects.get(user=request.user)
         
            course = student.course
            if course : 
                subjects = Subject.objects.filter(course = course)
            else:
                subjects =[] 
            
        except Student.DoesNotExist:
            print('No student found for the user')
            return redirect('/') 
    return render(request, 'view_subjects.html', {'subjects': subjects})

def divisions(request):
    divisions = Division.objects.all()
    return render(request, 'adminApp/manage_division.html', {'divisions': divisions})

def courses(request):
    courses = Course.objects.all()


