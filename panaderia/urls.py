from knox import views as knox_views
from django.urls import path
from .views import CajaAPI, PedidoAPI, DeliveryAPI

urlpatterns = [
    path('caja/', CajaAPI.as_view(), name='caja/'),
    path('pedido/', PedidoAPI.as_view(), name='pedido/'),
    path('delivery/', DeliveryAPI.as_view(), name='pedido/'),
]