from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import ExtendedUser
from django.shortcuts import get_object_or_404

from studentApp.models import Course 
from adminApp.models import Subject
from .forms import SubjectForm


# Create your views here.
def signin(request):
    if request.method == "POST":
        user_type = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate( request,username=email, password=password)
        if user is not None:
            ex_user = ExtendedUser.objects.get(user=user.id)
            if ex_user.user_type == user_type:
                print("User Type Correct!")
                # redirect to corresponding dashboard
                if user_type == "admin":
                    login(request, user)
                    return redirect('/')
                elif user_type == "student":
                    login(request, user)
                    return redirect('/student')
                elif user_type == "staff":
                    login(request, user)
                    return redirect('/staff')
        else:
            print("Invalid Credentials!!")
            return redirect('/signin')
        
    return render(request, 'signin.html')



def dashboard(request):
    return render(request, 'adminApp/index.html')


def courses(request):
    courses = Course.objects.all()
    return render(request, 'adminApp/manage_course.html', {'courses': courses})

def subject(request):
    subjects = Subject.objects.all()
    return render(request, 'adminApp/manage_subject.html', {'subjects': subjects})

def add_subject(request) :
    if request.method == "POST":
        form =SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/manage-subject")
        data = Subject.objects.all()
    else:
        form =SubjectForm()
        data = Subject.objects.all()
    return render(request, 'adminApp/add_subject.html', {'data':data, 'form' : form})




    

def update_subject(request, id):
    if request.method == "POST":
        pi = Subject.objects.get(pk=id)
        fm = SubjectForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect("/manage-subject")
    else :
        pi= Subject.objects.get(pk=id)
        fm =SubjectForm(instance=pi)
    return render(request, 'adminApp/update_subject.html', {'form':fm})
    
    



def delete_subject(request, id):
    pi = get_object_or_404(Subject, pk=id)  # Handle case where subject doesn't exist
    print("subj id", pi)
    if request.method == "POST":
        pi.delete()
        print("deleted")
        return HttpResponseRedirect("/manage-subject")
    
    # If a GET request is made, redirect or show a confirmation page
    return redirect("/manage-subject") 