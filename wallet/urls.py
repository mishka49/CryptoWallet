from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('my_wallets/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]