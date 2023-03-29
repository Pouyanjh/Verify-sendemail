
from email import message
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import user, Product
import uuid
from .serializer import RegisterSerializer, ProductSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username,
        token['email'] = user.email,
        # ...

        return token
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        if not user.is_email_verified:
             raise serializers.ValidationError(
                {"auth error": "Please verify your email address."}
            )


        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        uid = str(uuid.uuid4())
        user.activation_key = uid
        user.save()

        subject = 'Verify your email'
        message = f'Please verify your email address by clicking on this link http://127.0.0.1:8000/account-verify/{uid}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
    


class GetListProduct(APIView):
    def get(self, request):
        products =  Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

    
class VerifyEmail(APIView):
    def get(self, request, uid):
        User = None  # define the User object before using it in try block
        try:
            User = user.objects.get(activation_key=uid)
            User.is_email_verified = True
            User.activation_key = ''
            User.save()
            return Response({'message': 'Email verified successfully'}, status.HTTP_200_OK)
        
        except user.DoesNotExist:
            return Response({'message': 'Invalid activation link'}, status.HTTP_400_BAD_REQUEST)



        
















