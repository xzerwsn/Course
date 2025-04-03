from django.urls import path
from .views import register, user_login, user_logout, edit_profile, view_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', view_profile, name='view_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
