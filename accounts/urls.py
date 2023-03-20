from django.urls import path

from . import views

urlpatterns = [
    path("accounts/", views.CreateAccountsView.as_view()),
    path("accounts/<pk>/", views.UpdateAccountsView.as_view()),
    path("login/", views.LoginAccountView.as_view()),
]