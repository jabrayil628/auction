from django.urls import path
from .views import SignUpView, CustomLoginView,SettingsView,ContactMessageView,UserProfilUpdateView#,UserProfilView
from django.contrib.auth.views import LoginView,LogoutView
app_name='user_app'
urlpatterns = [
    path('register/',SignUpView.as_view(),name='register'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view() ,name="logout"),
    path('user-profile/',UserProfilUpdateView,name="profile"),
    path('send-message/',ContactMessageView.as_view() ,name="send-message"),
    path('change-password/',SettingsView.as_view() ,name="change-password"),
    # path('update/', UserProfilUpdateView,name='update')
    #      name='user-detail'),
    
]
