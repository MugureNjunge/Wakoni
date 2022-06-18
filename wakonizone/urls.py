from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
# from django.urls import reverse_lazy
# from django.conf import settings
# from django.conf.urls.static import static
# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('',views.index, name='index'),

    path('sign-up/',views.register,name='sign-up'),
    path('accounts/sign-in/',views.signin,name='sign-in'),
    path('sign-out/', views.signout, name='sign-out'),

    path('locality/',views.UserLocality,name='locality'),

    path('profile/edit/', views.EditProfile, name='editprofile'),
    
   

]