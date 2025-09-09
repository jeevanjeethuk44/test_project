from django.urls import path
from .views import GenerateOTPView, VerifyOTPView, UserDetailView

urlpatterns = [
    path('generate-otp/', GenerateOTPView.as_view(), name='generate-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
]
