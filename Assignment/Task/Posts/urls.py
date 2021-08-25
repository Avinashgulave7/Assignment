from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('',views.home,name='home'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('addpost/', views.AddPostView.as_view(), name='addpost'),
    path('add/', views.addpost),
    path('update/<id>', views.updatepost, name='update'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]
