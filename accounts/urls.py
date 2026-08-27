from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("", views.settings_view, name="settings"),
    path("delete-account/", views.delete_account_request, name="delete_account_request"),
    path("delete-account/sent/", views.delete_account_sent, name="delete_account_sent"),
    path("delete-account/confirm/<str:token>/", views.delete_account_confirm, name="delete_account_confirm"),
]
