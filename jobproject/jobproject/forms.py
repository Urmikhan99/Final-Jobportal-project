from django import forms 
from jobApp.models import *

class addjobform(forms.ModelForm):
    class Meta:
        model=JobModel
        fields='__all__'
        exclude=['created_by']
        widgets={
        'deadline':forms.DateInput(attrs={'type':'date','class':'date-field'}),
        }

class applyjobform(forms.ModelForm):
    class Meta:
        model=ApplyJobModel
        fields=['skills','resume','seeker_profile_pic']
        