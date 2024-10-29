from django.urls import path
from .views import CryptoWalletBalanceView

urlpatterns = [
    path('crypto_wallet/balance/<str:wallet_id>/<str:user_id>/', CryptoWalletBalanceView.as_view(), name='crypto_wallet_balance')
]