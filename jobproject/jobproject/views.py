from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from jobApp.models import *
from jobproject.forms import *


def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_type=request.POST.get('user_type')
        city=request.POST.get('city')
        gender=request.POST.get('gender')
        profile_picture=request.FILES.get('profile_picture')
        email=request.POST.get('email')
        
        if password==confirm_password:
            user = CustomUserModel.objects.create_user(
                username=username,
                password=password,
                user_type=user_type,
                city=city,
                gender=gender,
                profile_picture=profile_picture,
                email=email,
            )
            user.save()
            if user_type=="recruiter":
                user_tp=RecruiterModel.objects.create(recruiter_user=user)
            if user_type=="seeker":
                user_tp=SeekerModel.objects.create(seeker_user=user)
            user_tp.save()
            return redirect('signin')
    return render(request,'common/signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'common/signin.html')

@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')


@login_required
def addjob(request):
    if request.method == 'POST':
        form=addjobform(request.POST,request.FILES)
        if form.is_valid():
            addjob=form.save(commit=False)
            addjob.created_by=request.user
            addjob.save()
            return redirect('viewjob')
    else:
        form=addjobform()
    context={
        'form':form
    }
    return render(request,'recruiter/addjob.html',context)

def viewjob(request):
    jobview=JobModel.objects.all()
    context={
        'jobview': jobview
    }
    return render(request,'recruiter/viewjob.html',context)


def editjob(request,id):
    jobid=JobModel.objects.get(id=id)
    
    if request.method == 'POST':
        form=addjobform(request.POST,request.FILES,instance=jobid)
        if form.is_valid():
            addjob=form.save(commit=False)
            addjob.created_by=request.user
            addjob.save()
            return redirect('viewjob')
    else:
        form=addjobform(instance=jobid)
        
    context={
        'form':form
    }
    return render(request,'recruiter/editjob.html',context)

@login_required
def deletejob(request,id):
    job=get_object_or_404(JobModel,id=id)
    job.delete()
    return redirect('viewjob')

@login_required
def applyjob(request,id):
    applyjob=JobModel.objects.get(id=id)
    if request.method == 'POST':
        form=applyjobform(request.POST,request.FILES)
        if form.is_valid():
            applyform=form.save(commit=False)
            applyform.applicant=request.user
            applyform.applied_job=applyjob
            
            applyform.save()
            return redirect('appliedjob')
    else:
        form=applyjobform()
        
    context={
        'form':form
    }

    return render(request,'seeker/applyjob.html',context)




@login_required
def baseprofile(request):
 return render(request,'profile/baseprofile.html')

@login_required
def Recruiterprofile(request):
 return render(request,'profile/Recruiterprofile.html')

@login_required
def appliedjob(request):
 return render(request,'profile/appliedjob.html')


@login_required
def educationprofile(request):
 return render(request,'profile/educationprofile.html')


@login_required
def Seekerprofile(request):
 return render(request,'profile/Seekerprofile.html')

@login_required
def workprofile(request):
 return render(request,'profile/workprofile.html')