from django.urls import path, include
from .views import (
    WalletCreateView,
    WalletActivateView,
    WalletDisableView,
    WalletAddMoneyView,
    WalletWithdrawMoneyView,
)

urlpatterns = [
    

    path('create/', WalletCreateView.as_view(), name='wallet_create'),
    path('activate/', WalletActivateView.as_view(), name='wallet_activate'),
    path('disable/', WalletDisableView.as_view(), name='wallet_disable'),
    path('addmoney/', WalletAddMoneyView.as_view(), name='wallet_addmoney'),
    path('withdraw/', WalletWithdrawMoneyView.as_view(), name='wallet_withdraw'),
]



