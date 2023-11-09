from django.urls import path
import userapp.views

urlpatterns = [
    path('signup/', userapp.views.signup, name = 'signup'),
    path('login/', userapp.views.login, name = 'login'),
    path('logout/', userapp.views.logout, name = 'logout'),
]
