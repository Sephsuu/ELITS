from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('shop/', views.shop, name='shop'),
    path('who_we_are/', views.who_we_are, name='who_we_are'),
    path('signup/', views.signup, name='signup'),
    path('verify_email/<str:token>/', views.verify_email, name='verify_email'),
    path('login/', views.login, name='login'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.logout, name='logout'),
]

