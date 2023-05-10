from django.urls import path

from . import views

urlpatterns = [
    path("accounts/", views.CreateAccountsView.as_view()),
    path("accounts/<slug:username>/", views.UpdateAccountView.as_view()),
    path("login/", views.LoginJWTView.as_view()),
    path("profile/<slug:username>/", views.RetrieveAccountsView.as_view())
    # path("token/refresh/", views.TokenRefreshView.as_view()),
]
