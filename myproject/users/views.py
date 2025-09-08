import random
from datetime import timedelta
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import PhoneSerializer, VerifyOTPSerializer

class GenerateOTPView(generics.GenericAPIView):
    serializer_class = PhoneSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']

        otp = str(random.randint(100000, 999999))
        otp_expiry = timezone.now() + timedelta(minutes=10)

        user, created = User.objects.get_or_create(phone_number=phone_number)
        user.otp = otp
        user.otp_expiry = otp_expiry
        user.save()

        # In a real application, you would send this OTP via SMS.
        # For this demo, we'll just print it to the console.
        print(f"OTP for {phone_number}: {otp}")

        return Response({"message": "OTP generated successfully."}, status=status.HTTP_200_OK)

class VerifyOTPView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        otp = serializer.validated_data['otp']

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if user.otp != otp or timezone.now() > user.otp_expiry:
            return Response({"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)

        # OTP is valid, clear it and generate tokens
        user.otp = None
        user.otp_expiry = None
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
