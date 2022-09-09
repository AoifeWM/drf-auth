from django.urls import path
from .views import SaleList, SaleDetail

urlpatterns = [
    path('', SaleList.as_view(), name="sale_list"),
    path('<int:pk>', SaleDetail.as_view(), name="sale_detail"),
]