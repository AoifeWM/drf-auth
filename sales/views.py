from django.shortcuts import render
from rest_framework import generics
from .serializer import SaleSerializer
from .models import Sale
from .permissions import OwnerOrSafeOnly


class SaleList(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (OwnerOrSafeOnly,)


class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (OwnerOrSafeOnly,)
