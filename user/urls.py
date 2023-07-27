from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import SignupView

app_name='user'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('signup/', SignupView.as_view(), name='signup'),
    
]



