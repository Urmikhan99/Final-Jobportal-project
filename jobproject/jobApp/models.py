from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    USER_TYPE={
        ('seeker','Job Seeker'),
        ('recruiter','Job Recruiter'),
    }
    user_type=models.CharField(choices=USER_TYPE,max_length=100)
    city=models.CharField(max_length=100)
    GENDER={
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    }    
    gender=models.CharField(choices=GENDER,max_length=100)
    profile_picture=models.ImageField(upload_to='media/profile_picture')
    
    # basic info 
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    hobby=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class RecruiterModel(models.Model):
    # contact
    mobile_number=models.CharField(max_length=100)
    company_address=models.CharField(max_length=100)
    
    recruiter_user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruitermodel')
    
    def __str__(self):
        return self.recruiter_user.username
    
class SeekerModel(models.Model):
    # education
    edu_name=models.CharField(max_length=100)
    edu_institute=models.CharField(max_length=100)
    edu_location=models.CharField(max_length=100)

    # work exprerience
    work_name=models.CharField(max_length=100)
    work_location=models.CharField(max_length=100)
    work_time=models.CharField(max_length=100)
    
    seeker_user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekermodel')
    def __str__(self):
        return self.seeker_user.username
    
class JobModel(models.Model):
    job_title=models.CharField(max_length=100)
    company_description=models.TextField()
    company_logo=models.ImageField(upload_to='media/company_logo')
    company_name=models.CharField(max_length=100)
    company_location=models.TextField()
    qualifications=models.CharField(max_length=100)
    deadline=models.DateField()
    salary=models.CharField(max_length=100)
    created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.created_by.username

class ApplyJobModel(models.Model):
    applicant=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,related_name='applicantinfo')
    applied_job=models.ForeignKey(JobModel,on_delete=models.CASCADE)
    skills=models.CharField(max_length=100)
    resume = models.FileField(upload_to='media/seeker_resume')
    seeker_profile_pic = models.ImageField(upload_to='media/seeker_profile_pic')
    qualifications = models.TextField()
    status=models.CharField(max_length=100, default="Pending")
    date_fix=models.DateField(null=True)
    def __str__(self):
        return self.applicant.username