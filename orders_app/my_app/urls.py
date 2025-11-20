from my_app.views import ProductView
from rest_framework import routers
from django.urls import path

app_name = "my_app"

routers = routers.DefaultRouter()

urlpatterns = []

routers.register(
    r'products', ProductView, basename="products"
)

urlpatterns += routers.urls