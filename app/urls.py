from django.urls import path
from app.views import home_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home_view, name='home'),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]