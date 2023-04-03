from rest_framework import serializers
from .models import Wallet, customer

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields= ('name','email','phone_no')