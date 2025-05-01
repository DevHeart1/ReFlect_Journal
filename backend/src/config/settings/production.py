from .base import * # Inherit from base settings

# Override base settings for production

DEBUG = config("DEBUG", default=False, cast=bool) # Ensure Debug is False

# Configure allowed hosts from environment variable
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Security settings for production
# SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=True, cast=bool) # Handled by Render proxy
# SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", default=31536000, cast=int) # 31536000 = 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True, cast=bool)
# SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", default=True, cast=bool)
# SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", default=True, cast=bool)
# CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", default=True, cast=bool)
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https") # If using a proxy like Render's

# CORS settings for production (allow Vercel frontend)
CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())
# Example: CORS_ALLOWED_ORIGINS=https://your-frontend.vercel.app,https://www.your-frontend.vercel.app

# Configure logging for production (e.g., send to stdout for Render to capture)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "json": { # Example JSON formatter
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO", # Adjust level as needed
            "class": "logging.StreamHandler",
            "formatter": "verbose", # Or 'json'
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO", # Adjust level as needed
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": config("DJANGO_LOG_LEVEL", default="INFO"),
            "propagate": False,
        },
        "django.db.backends": {
             "handlers": ["console"],
             "level": config("SQL_LOG_LEVEL", default="INFO"), # Set to DEBUG to see SQL queries
             "propagate": False,
        },
    },
}

# Configure email backend for production (e.g., SendGrid, Mailgun)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# Static files storage (e.g., Whitenoise for Render)
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Add 'whitenoise.middleware.WhiteNoiseMiddleware' to MIDDLEWARE (usually right after SecurityMiddleware)

# Media files storage (Supabase Storage) - Configuration needed
# DEFAULT_FILE_STORAGE = 'path.to.your.SupabaseStorage' # Custom storage backend
