from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from wallets.views import WalletsView, WalletsCreatorView, WalletsInfoView

urlpatterns = [
    path('my_wallets/', WalletsView.as_view(), name='wallet'),
    path('create/<str:wallet_type>', WalletsCreatorView. as_view, name='creator'),
    path('balance/<str:publick_key>', WalletsInfoView.as_view(), name='balance'),
]