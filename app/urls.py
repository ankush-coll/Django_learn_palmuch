from django.urls import path
from .views import data,photos, home,songs, register, verify_otp, admin_dashboard

urlpatterns=[
    path('home/',home,name='home'),
    path('data/',data,name='data'),
    path('photos/',photos,name='photos'),
    path('songs/',songs,name='songs'),
    path("register/", register, name="register"),
    path("verify-otp/", verify_otp, name="verify-otp"),
    path("admin_dash/",admin_dashboard,name='ad-dash'),
]