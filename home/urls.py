from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'home'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    path('success-contact/',views.successView,name='success_contact'),
    
    path('change-password/', views.change_password, name='change_password'),
    path('search/',views.search_text,name='search-text'),
    path('login/',views.loginUser.as_view(),name='loginUser'),
    path('register/',views.registerUser,name='registerUser'),
    path('register-teacher/',views.registerTeacher.as_view(),name='registerTeacher'),
    path('logout/',LogoutView.as_view(),name='logoutUser'),
]

