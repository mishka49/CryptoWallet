from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from wallets.views import WalletsView, WalletsCreatorView, WalletTypeView, WalletsInfoView

urlpatterns = [
    path('my_wallets/', WalletsView.as_view(), name='wallet'),
    path('create/', WalletsCreatorView. as_view(), name='creator'),
    path('types/', WalletTypeView.as_view(), name='types'),
    path('balance/<str:public_key>', WalletsInfoView.as_view(), name='balance'),
]