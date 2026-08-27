from django.conf import settings
from django.core import signing


DELETE_ACCOUNT_SALT = "accounts.delete-account"


def create_delete_account_token(user):
    payload = {
        "user_id": user.pk,
        "email": user.email,
    }

    return signing.dumps(
        payload,
        salt=DELETE_ACCOUNT_SALT,
        compress=True,
    )


def validate_delete_account_token(token):
    try:
        return signing.loads(
            token,
            salt=DELETE_ACCOUNT_SALT,
            max_age=settings.ACCOUNT_DELETE_TOKEN_MAX_AGE,
        )
    except (signing.BadSignature, signing.SignatureExpired):
        return None

