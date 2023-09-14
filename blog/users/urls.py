# urls.py
from django.urls import path
from .views import UserRegistrationView,UserLoginView,UserLogoutView,UserDetailView,MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshSlidingView,
)
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
]