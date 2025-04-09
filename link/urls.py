"""LinkManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.contrib.auth import views as authViews


urlpatterns = [
    path('',views.index, name="LinkHome" ),
    path("about/",views.about, name="AboutUs"),
    path("contact/",views.contact, name="ContactUs"),
    path("signup/",views.signup, name="SignUp"),
    path("login/",views.handlelogin, name="Login"),
    path("logout/",views.handlelogout, name="Logout"),
    path('changepassword/', views.PasswordChange, name='ChangePassword'),
    path('passwordreset/', authViews.PasswordResetView.as_view(template_name='link/password_reset_form.html'), name='password_reset'),

   	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(template_name='link/password_reset_done.html'), name='password_reset_done'),

   	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='link/password_reset_confirm.html'), name='password_reset_confirm'),

   	path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(template_name='link/password_reset_complete.html'), name='password_reset_complete'),   

    path("select/",views.selectchoice, name="Select"),
    path("addlinks/",views.addlinks, name="AddLinks"),
    path("profile/<slug:namers>/",views.profile, name="Profile"),
    path("updatelinks/",views.updatelinks, name="UpdateLinks"),
    path("deletelinks/",views.deletelinks, name="DeleteLinks"),
    
] 
 