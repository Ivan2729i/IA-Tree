import os
from pathlib import Path
from dotenv import load_dotenv



BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = 'django-insecure-)&m_2593a$4i%7f!qp0gt0!6bwl+1+2h!_=r=lpkyx(txa3frd'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'core',
    'accounts',
    'analysis',
    'reports',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.app_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
    {
        "NAME": "accounts.validators.StrongPasswordValidator",
    },
]


# Internationalization
# Internationalization
LANGUAGE_CODE = "es-mx"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"


# Email
MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "OPTIONS": {
            "host": os.getenv("MAIL_HOST", ""),
            "port": int(os.getenv("MAIL_PORT", "587")),
            "username": os.getenv("MAIL_USERNAME", ""),
            "password": os.getenv("MAIL_PASSWORD", ""),
            "use_tls": os.getenv("MAIL_USE_TLS", "True").lower() == "true",
            "timeout": 10,
        },
    },
}

DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL",
    "Sistema de Análisis <no-reply@localhost>"
)


APP_NAME = "Sistema de Análisis de Arbolado"


# =========================================================
# AUTENTICACIÓN
# =========================================================

AUTH_USER_MODEL = "accounts.User"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

LOGIN_URL = "account_login"
LOGIN_REDIRECT_URL = "core:dashboard"
ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"


# =========================================================
# DJANGO ALLAUTH
# =========================================================

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

ACCOUNT_UNIQUE_EMAIL = True

# El usuario DEBE verificar su correo para poder iniciar sesión.
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Usaremos enlace por correo, no código.
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = False

# No iniciar sesión automáticamente después de verificar el correo.
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

# Después de confirmar el correo, mandar al login.
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_login"

# Los enlaces de verificación duran 3 días.
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

# Asunto de los correos.
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Sistema de Análisis] "

# Mantener la opción "Mantener sesión iniciada".
ACCOUNT_SESSION_REMEMBER = None

# Seguridad adicional: avisos por correo ante ciertos cambios de cuenta.
ACCOUNT_EMAIL_NOTIFICATIONS = True

# Una sola dirección de correo por cuenta.
ACCOUNT_MAX_EMAIL_ADDRESSES = 1

# Reautenticación para operaciones sensibles gestionadas por Allauth.
ACCOUNT_REAUTHENTICATION_REQUIRED = True
ACCOUNT_REAUTHENTICATION_TIMEOUT = 300

# Enlace para eliminar cuenta será válido durante 1 hora.
ACCOUNT_DELETE_TOKEN_MAX_AGE = 60 * 60

ACCOUNT_ADAPTER = "accounts.adapters.AccountAdapter"

# =========================================================
# GOOGLE OAUTH
# =========================================================

GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID", "")
GOOGLE_OAUTH_CLIENT_SECRET = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET", "")

GOOGLE_OAUTH_ENABLED = bool(
    GOOGLE_OAUTH_CLIENT_ID and GOOGLE_OAUTH_CLIENT_SECRET
)

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": GOOGLE_OAUTH_CLIENT_ID,
            "secret": GOOGLE_OAUTH_CLIENT_SECRET,
            "key": "",
        },

        "SCOPE": [
            "profile",
            "email",
        ],

        "AUTH_PARAMS": {
            "access_type": "online",
        },

        "OAUTH_PKCE_ENABLED": True,
    }
}


SOCIALACCOUNT_AUTO_SIGNUP = True

SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
