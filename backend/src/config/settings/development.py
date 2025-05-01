from .base import * # Inherit from base settings

# Override base settings for development

DEBUG = config("DEBUG", default=True, cast=bool) # Enable Debug in development

# Add development-specific apps if needed
# INSTALLED_APPS += ["django_extensions", "debug_toolbar"]

# Add development-specific middleware if needed
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# Configure development database if different from default (e.g., local postgres)
# DATABASES = { ... }

# Allow all hosts for local development convenience
ALLOWED_HOSTS = ["*"]

# CORS settings for development (allow frontend dev server)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # Assuming frontend runs on 3000
    "http://127.0.0.1:3000",
]
# Or allow all for simplicity in local dev:
# CORS_ALLOW_ALL_ORIGINS = True

# Internal IPs for Django Debug Toolbar (if used)
# INTERNAL_IPS = [
#     "127.0.0.1",
# ]

# Email backend for development (prints to console)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
