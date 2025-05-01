# ReFlect Journaling App - Backend Development Guidelines

**Version:** 1.1
**Date:** May 1, 2025

## 1. Introduction

This document establishes the definitive standards, conventions, and best practices for backend development of the ReFlect Journaling App API, built using Django and Python. The primary goal is to create a secure, scalable, maintainable, and performant API that reliably serves the frontend application and integrates seamlessly with external services like Supabase and Gemini AI. Consistency and adherence to these guidelines are paramount for team collaboration and long-term project success.

## 2. Core Technologies & Libraries

*(Refer to `tech_stack.md` for the definitive specification)*

*   **Language:** Python (v3.10+)
*   **Framework:** Django (v4+) + Django REST Framework (DRF)
*   **Database:** Supabase (Managed PostgreSQL v15+)
*   **ORM:** Django ORM
*   **Object Storage:** Supabase Storage
*   **Authentication Integration:** Supabase Auth (JWT Verification)
*   **API Specification:** `drf-spectacular` (OpenAPI 3)
*   **Asynchronous Tasks (Future):** Celery + Redis/RabbitMQ
*   **Linting:** Flake8 (with plugins)
*   **Formatting:** Black
*   **Type Checking:** Mypy
*   **Testing:** `pytest`, `pytest-django`, `factory-boy`, `pytest-mock`
*   **Environment Variables:** `python-decouple` or `django-environ`
*   **CORS:** `django-cors-headers`
*   **Security Headers:** Django's built-in middleware
*   **Deployment:** Docker + Render

## 3. Code Style & Formatting

*   **Automation:** Black, Flake8, and Mypy are mandatory and configured via `pre-commit` hooks. All code must pass these checks before merging.
*   **Configuration:** Utilize shared configurations committed to the repository (`pyproject.toml`, `.flake8`). Configure Mypy for strict type checking.
*   **Style Guide:** Strictly adhere to **PEP 8**. Use Black for automatic formatting to ensure consistency.
*   **Type Hinting:** Comprehensive type hinting is mandatory for all function signatures, variables, and class attributes. Use standard Python typing (`typing` module).
*   **Docstrings:** Write clear Google-style docstrings for all modules, classes, methods, and functions, explaining purpose, arguments, and return values.
*   **Naming Conventions:** Follow PEP 8 (`lower_snake_case` for variables/functions/modules, `CapWords` for classes, `UPPER_SNAKE_CASE` for constants).

## 4. Project Structure (Django)

Employ a structured approach with clear separation between the Django project configuration and individual apps representing features/domains. Placing apps within a source directory (e.g., `src/`) is recommended.

```
.dockerignore
.env
.env.example
.flake8
.gitignore
Dockerfile            # For Render deployment
docker-compose.yml    # For local development
manage.py
mypy.ini
pre-commit-config.yaml
pyproject.toml        # Defines dependencies (Poetry/PDM) or build system, Black/Mypy config
pytest.ini
README.md
requirements/         # Or use Poetry/PDM for dependency management
  ├── base.txt
  ├── dev.txt
  └── prod.txt
src/                  # Main source directory
├── apps/               # Django applications (features/domains)
│   ├── __init__.py
│   ├── common/         # Shared utilities, base classes, custom middleware
│   │   └── ...
│   ├── users/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py     # User profile, preferences (linking to Supabase Auth ID)
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── services.py   # Business logic related to users
│   │   ├── urls.py
│   │   ├── views.py      # DRF ViewSets/APIViews
│   │   └── tests/
│   ├── journaling/
│   │   ├── __init__.py
│   │   ├── models.py     # JournalEntry, Tag, MoodLog models
│   │   ├── serializers.py
│   │   ├── services.py   # Logic for entry creation, AI triggering
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests/
│   └── ai/
│       ├── __init__.py
│       ├── clients.py    # Client for interacting with Gemini API
│       ├── services.py   # Service layer for AI tasks (sentiment analysis)
│       └── tasks.py      # Celery tasks (if using async)
├── config/             # Django project configuration
│   ├── __init__.py
│   ├── settings/       # Split settings (base.py, development.py, production.py)
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py         # Root URL configuration (including API versioning)
│   ├── wsgi.py
│   └── asgi.py         # If using async features
└── staticfiles/        # Collected static files (less relevant for pure API)
```

## 5. API Design (DRF)

*   **Style:** Strictly RESTful. Use nouns for resources and standard HTTP methods for actions.
*   **Versioning:** Implement URL path versioning (e.g., `/api/v1/journal/entries/`).
*   **Specification:** Auto-generate OpenAPI 3 schema using `drf-spectacular`. Ensure serializers and views are correctly annotated for accurate schema generation.
*   **Serializers:**
    *   Use DRF serializers for input validation and output representation.
    *   Define explicit fields. Avoid `fields = '__all__'`.
    *   Use nested serializers for related objects where appropriate, but be mindful of performance (N+1 queries).
    *   Implement custom validation logic within serializers (`validate_<field>`, `validate()`).
*   **Views:**
    *   Use DRF Generic Views (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`) or ViewSets (`ModelViewSet`) for standard CRUD operations.
    *   Keep views focused on handling HTTP requests/responses and delegating business logic to service layers.
    *   Define `permission_classes`, `serializer_class`, `queryset` clearly.
*   **Pagination:** Use standard DRF pagination classes (e.g., `PageNumberPagination`) for list endpoints.
*   **Filtering:** Use `django-filter` for robust filtering capabilities on list endpoints.
*   **Responses:** Return consistent JSON responses. Use standard HTTP status codes correctly. Structure error responses clearly (DRF default or custom handler).

## 6. Database Interaction (Django ORM + Supabase)

*   **Models:** Define well-structured models in `models.py` with appropriate field types, relationships (`ForeignKey`, `ManyToManyField`), and constraints. Add `Meta` options for ordering, indexes, etc.
*   **QuerySets & Managers:** Utilize custom QuerySet methods and Managers to encapsulate reusable database queries and logic related to specific models.
*   **Performance:**
    *   Use `select_related` (for ForeignKey/OneToOne) and `prefetch_related` (for ManyToMany/Reverse ForeignKey) aggressively to prevent N+1 query problems, especially in serializers and list views.
    *   Use `values()` and `values_list()` for retrieving specific fields when full model instances are not needed.
    *   Use `defer()` and `only()` to control which fields are loaded.
    *   Analyze query performance using `django-debug-toolbar` during development.
    *   Define database indexes (`db_index=True`, `Meta.indexes`) for frequently queried fields.
*   **Transactions:** Use `django.db.transaction.atomic()` as a decorator or context manager for operations requiring atomicity (e.g., creating an entry and associated tags).
*   **Migrations:** Generate migrations (`makemigrations`) after every model change and apply them (`migrate`). Keep migrations small and focused. Write data migrations where necessary.

## 7. Authentication & Authorization

*   **Authentication:** Use **Django's built-in authentication system** combined with **Django REST Framework's token authentication** (e.g., **`djangorestframework-simplejwt`** for JWT). User registration and login will be handled by Django endpoints.
    *   *Note:* While Supabase Auth is available, managing users directly within Django provides more control over the user model and authentication flow within the backend. The frontend will authenticate against Django API endpoints.
*   **Password Hashing:** Handled by **Django's built-in password hashing system**.
*   **Authorization:** Use DRF's permission classes (`permissions.py`) based on Django's user model and groups/permissions.

## 8. Service Layer & Business Logic

*   **Separation of Concerns:** Extract business logic from views and models into dedicated service functions or classes (`services.py`).
*   **Responsibilities:** Services orchestrate operations, interact with models/managers, call external APIs (like Gemini), handle complex validation rules, and trigger side effects (like background tasks).
*   **Testability:** Services should be easily testable in isolation, mocking database interactions and external API calls.

## 9. Error Handling

*   **Custom Exception Handler:** Implement a custom DRF exception handler (configured in `settings.py`) to standardize error response formats (e.g., `{"errors": [{"code": "validation_error", "detail": "...", "field": "..."}]}`).
*   **Specific Exceptions:** Define custom exception classes for specific business logic errors.
*   **Logging:** Ensure all unhandled exceptions and significant errors are logged with detailed context (stack trace, request info).
*   **Validation:** Rely on DRF serializers for handling standard validation errors (returning 400 Bad Request).

## 10. Testing (pytest + pytest-django)

*   **Framework:** Use `pytest` as the test runner.
*   **Test Types:**
    *   **Unit Tests:** Test services, utility functions, serializer logic, custom managers/queryset methods in isolation. Mock database and external APIs (`unittest.mock` or `pytest-mock`).
    *   **Integration Tests:** Test DRF API views using `pytest-django`'s `APIClient`. These tests interact with the test database. Focus on request/response validation, permissions, and basic data manipulation.
*   **Test Database:** Configure `pytest-django` to use a separate test database, ideally PostgreSQL.
*   **Fixtures:** Use `pytest` fixtures for setting up test data and dependencies.
*   **Factories:** Use `factory-boy` to generate realistic model instances for testing.
*   **Coverage:** Aim for high test coverage (>85%) for backend code, measured using `pytest-cov`. Integrate coverage checks into CI.
*   **Assertions:** Write clear and specific assertions.

## 11. Environment Configuration

*   **Library:** Use `django-environ` or `python-decouple` to load configuration from environment variables and `.env` files.
*   **Settings Files:** Split Django settings into `base.py`, `development.py`, `production.py`, `test.py` for different environments. Production settings should load secrets strictly from environment variables.
*   **`.env` File:** Use `.env` only for local development. Provide a `.env.example` file documenting required variables. Never commit `.env`.

## 12. Security

*   **OWASP Top 10:** Be mindful of common vulnerabilities and Django/DRF mitigations.
*   **Input Validation:** Always validate data via DRF serializers.
*   **Permissions:** Enforce strict authorization using DRF permissions.
*   **Secrets Management:** Never hardcode secrets. Load from environment variables.
*   **Dependencies:** Regularly update dependencies and audit for vulnerabilities (`pip-audit`).
*   **HTTPS:** Ensure HTTPS is enforced (handled by Render).
*   **CORS:** Configure `django-cors-headers` restrictively for allowed origins (Vercel frontend URL).
*   **Security Headers:** Utilize Django's built-in security middleware (`SecurityMiddleware`, `XFrameOptionsMiddleware`, etc.) and potentially `django-csp`.
*   **Rate Limiting:** Implement rate limiting on sensitive endpoints using `django-ratelimit` or DRF's throttling.

## 13. Logging & Monitoring

*   **Configuration:** Configure Python's `logging` in `settings.py`. Use `structlog` for structured JSON logging if advanced processing is needed.
*   **Log Levels:** Use appropriate levels (DEBUG, INFO, WARNING, ERROR, CRITICAL). Be cautious with logging sensitive data.
*   **Integration:** Configure Render to forward logs to a preferred aggregation service (e.g., Datadog, Logtail).
*   **Monitoring:** Leverage Render's built-in metrics. Add custom application metrics using `django-prometheus` if needed. Integrate with error tracking services like Sentry.

## 14. Version Control (Git)

*   Follow the same guidelines as outlined in `frontend_guidelines.md` (GitHub Flow, Conventional Commits, PRs with reviews and CI checks).

By adhering to these comprehensive guidelines, we aim to build a robust, secure, and maintainable backend foundation for the ReFlect application.