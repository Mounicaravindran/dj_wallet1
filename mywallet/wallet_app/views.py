from http.client import ResponseNotReady, responses
from urllib import response
from rest_framework import generics
from .models import Wallet
from .serializers import WalletSerializer 


from django.contrib.auth.models import User
from django.shortcuts import render
from.models import customer

def create_customer(request):
    # get the user object
    user = User.objects.get(username='myuser')
    # create a new customer object and link it to the user object
    customer = customer.objects.create(user=user, name='Mouni', email='mouni@gmail.com', phone_no='1234567890')
    # render a success message
    return render(request, 'customer_created.html', {'customer': customer})


class WalletCreateView(generics.CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletActivateView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = True
        instance.save()
        serializer = self.get_serializer(instance)
        return response(serializer.data)

class WalletDisableView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return response(serializer.data)

class WalletAddMoneyView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        amount = request.data.get('amount')
        instance.balance += amount
        instance.save()
        serializer = self.get_serializer(instance)
        return response(serializer.data)

class WalletWithdrawMoneyView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        amount = request.data.get('amount')
        if instance.balance >= amount:
            instance.balance -= amount
            instance.save()
            serializer = self.get_serializer(instance)
            return responses(serializer.data)
        else:
            return response({'detail': 'Insufficient funds'}, status=400)
