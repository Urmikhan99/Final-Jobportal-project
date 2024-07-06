from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    USER_TYPE={
        ('seeker','Job Seeker'),
        ('recruiter','Job Recruiter'),
    }
    user_type=models.CharField(choices=USER_TYPE,max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    GENDER={
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    }    
    gender=models.CharField(choices=GENDER,max_length=100,null=True)
    profile_picture=models.ImageField(upload_to='media/profile_picture',null=True)
    
    father_name=models.CharField(max_length=100,null=True)
    mother_name=models.CharField(max_length=100,null=True)
    hobby=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.username

class RecruiterModel(models.Model):
    mobile_number=models.CharField(max_length=100,null=True)
    company_address=models.CharField(max_length=100,null=True)
    
    recruiter_user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruitermodel',null=True)
    
    def __str__(self):
        return self.recruiter_user.username
    
class SeekerModel(models.Model):
    edu_name=models.CharField(max_length=100,null=True)
    edu_institute=models.CharField(max_length=100,null=True)
    edu_location=models.CharField(max_length=100,null=True)


    work_name=models.CharField(max_length=100,null=True)
    work_location=models.CharField(max_length=100,null=True)
    work_time=models.CharField(max_length=100,null=True)
    
    seeker_user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekermodel',null=True)

    
class JobModel(models.Model):
    job_title=models.CharField(max_length=100,null=True)
    company_description=models.TextField(null=True)
    company_logo=models.ImageField(upload_to='media/company_logo',null=True)
    company_name=models.CharField(max_length=100,null=True)
    company_location=models.TextField(null=True)
    qualifications=models.CharField(max_length=100,null=True)
    deadline=models.DateField(null=True)
    salary=models.CharField(max_length=100,null=True)
    created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    


class ApplyJobModel(models.Model):
    applicant=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,related_name='applicantinfo',null=True)
    applied_job=models.ForeignKey(JobModel,on_delete=models.CASCADE)
    skills=models.CharField(max_length=100,null=True)
    resume = models.FileField(upload_to='media/seeker_resume',null=True)
    seeker_profile_pic = models.ImageField(upload_to='media/seeker_profile_pic',null=True)
    status=models.CharField(max_length=100, default="Pending",null=True)
