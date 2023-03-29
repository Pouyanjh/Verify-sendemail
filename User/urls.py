from django.urls import path
from .views import RegisterView, MyTokenObtainPairView, GetListProduct, VerifyEmail
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('product/', GetListProduct.as_view()),
    path('account-verify/<str:uid>/', VerifyEmail.as_view(), name='verify-email'),




]