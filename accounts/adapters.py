from django.urls import reverse
from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def get_password_change_redirect_url(self, request):
        return reverse("accounts:settings") + "#security"

