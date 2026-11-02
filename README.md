# user_accounts_django

A complete **user account system** in Django, built entirely on Django's built-in auth views: sign up, log in and out, change your password, and reset a forgotten password by email.

Based on the tutorial [How to reset password in Django](https://medium.com/@renjithsraj/how-to-reset-password-in-django-bd5e1d6ed652).

## Features

- Sign up
- Log in and log out
- Change password
- Password reset by email (form → email → confirm → complete)
- Login-protected pages, shown both ways: a function view with `@login_required` (`/secret/`) and a class view with `LoginRequiredMixin` (`/secret2/`)

## Running

```bash
cd myWeb
python -m venv venv && source venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver        # http://localhost:8000
```

Password reset emails need email settings. For local testing, add this to `myWeb/settings.py` so emails are printed to the console:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

## Routes

| Path | Description |
|---|---|
| `/` | Home |
| `/signup/` | Register |
| `/accounts/login/`, `/accounts/logout/` | Log in / log out |
| `/accounts/password_change/` | Change password |
| `/accounts/password_reset/` | Reset a forgotten password |
| `/secret/`, `/secret2/` | Login-protected pages |

## Configuration

Secrets are read from **environment variables**, so nothing sensitive lives in the code. Copy [`.env.example`](.env.example) to `.env` (it is git-ignored) or export the variables in your shell:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django `SECRET_KEY`. If unset, a random key is generated at startup (fine for local dev). |

The same values are stored as **GitHub Actions secrets** on this repo (*Settings → Secrets and variables → Actions*), so CI/CD workflows can use them as `${{ secrets.NAME }}`.
