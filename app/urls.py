from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from app.views import *
urlpatterns = [ 
    path('data/', hotel_image_view, name = 'image_upload'), 
    path('signup/',user_signup,name='signup'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('',Show, name = 'hotel_images'),
     path('comment/',comment, name='comt'),
] 
  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
