from flask import request, abort
from kyvue.configs.env_loader import SECRET_TOKEN


def check_secret_token():
    """
    Middleware function to allow access based on a secret token.
    """
    token = request.headers.get("Authorization")  # Get the token from the 'Authorization' header
    if token != SECRET_TOKEN:
        abort(403) 