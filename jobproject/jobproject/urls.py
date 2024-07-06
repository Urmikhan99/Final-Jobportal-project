from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobproject.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('addjob/',addjob,name='addjob'),
    path('viewjob/',viewjob,name='viewjob'),
    path('editjob/<str:id>',editjob,name='editjob'),
    path('deletejob/<str:id>',deletejob,name='deletejob'),
    path('applyjob/<str:id>',applyjob,name='applyjob'),
    
    path('appliedjob/',appliedjob,name='appliedjob'),
    path('Recruiterprofile/',Recruiterprofile,name='Recruiterprofile'),
    path('baseprofile/',baseprofile,name='baseprofile'),
    path('Seekerprofile/',Seekerprofile,name='Seekerprofile'),
    path('educationprofile/',educationprofile,name='educationprofile'),
    path('workprofile/',workprofile,name='workprofile'),
    path('workprofile/',workprofile,name='workprofile'),
    
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
