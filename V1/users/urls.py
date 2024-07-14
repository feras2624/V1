from django.urls import path 
from . import views
urlpatterns = [
    path('user/login',views.login_view,name='login_view'),
    path('user/home',views.home_view,name='home_view'),
    path('user/logout',views.logout_view,name='logout_view'),
]
