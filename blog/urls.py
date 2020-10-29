from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path("signout", views.signout, name="signout"),
    path('ajax/', views.ajaxx, name='ajax'),


]