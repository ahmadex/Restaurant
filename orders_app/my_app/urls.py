from my_app.views import ProductView, OrderView
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "my_app"

routers = routers.DefaultRouter()

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

routers.register(
    r'products', ProductView, basename="products"
)
routers.register(
    r'orders', OrderView, basename="orders"
)
urlpatterns += routers.urls