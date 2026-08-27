from django.conf import settings


def app_settings(request):
    return {
        "APP_NAME": settings.APP_NAME,
        "GOOGLE_OAUTH_ENABLED": settings.GOOGLE_OAUTH_ENABLED,
    }
