from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import UserLoginView, UserRegistrationView, UserProfileView, upload_image, gallery, delete_image

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView, name='login'),
    path('registration/', UserRegistrationView, name='registration'),
    path('profile/', login_required(UserProfileView), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('upload/', login_required(upload_image), name='upload_image'),
    path('gallery/', login_required(gallery), name='gallery'),
    path('delete_image/<int:image_id>/', delete_image, name='delete_image'),
    # path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]