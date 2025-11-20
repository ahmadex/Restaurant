from my_app.views import home
from django.urls import path

app_name = "my_app"

urlpatterns = [
    path('home', home, name="home")
]

