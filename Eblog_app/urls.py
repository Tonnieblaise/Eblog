from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('index', views.home,name="home"), #Guardians was taking me to profile, hence, this
    path('edit', views.edit,name="edit"),
    path('email', views.email,name="email"),
    path('content', views.content,name="content"),
    path('profile', views.profile,name="profile"),
    path('login', views.login,name="login"),
    path('signup', views.signup,name="signup"),
    path('add_email', views.add_email,name="add_email")
]