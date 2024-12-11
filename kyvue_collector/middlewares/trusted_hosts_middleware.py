from flask import request, abort
from kyvue_collector.configs.env_loader import ALLOWED_HOSTS

def check_trusted_server():
    """
    Middleware function to allow only trusted IPs.
    """
    client_ip = request.remote_addr
    if client_ip not in ALLOWED_HOSTS:
        abort(403)
