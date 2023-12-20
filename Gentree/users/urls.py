from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import UserLoginView, UserRegistrationView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView, name='login'),
    path('registration/', UserRegistrationView, name='registration'),
    path('profile/', login_required(UserProfileView), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]