from django.urls import path

from . import views

urlpatterns = [
    path("accounts/", views.CreateAccountsView.as_view()),
    path("accounts/<pk>/", views.UpdateAccountView.as_view()),
    path("login/", views.LoginJWTView.as_view()),
    path("profile/<pk>/", views.RetrieveAccountsView.as_view())
    # path("token/refresh/", views.TokenRefreshView.as_view()),
]
