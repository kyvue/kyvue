from flask import Flask, jsonify
from .middlewares.trusted_hosts_middleware import check_trusted_server
from .middlewares.token_auth_middleware import check_secret_token
from .configs.env_loader import AUTH_ENABLED, ENABLE_TOKEN_BASED_ACCESS
from .plugins import DockerPlugin, SystemPlugin


app = Flask(__name__)


# Allowed endpoints
ALLOWED_ENDPOINTS = ['/metrics']


# Register middleware
@app.before_request
def before_request():
    if AUTH_ENABLED:
        check_trusted_server()

        if ENABLE_TOKEN_BASED_ACCESS:
            check_secret_token()


@app.errorhandler(403)
def forbidden_error(e):
    """
    Custom handler for forbidden errors.
    """
    return jsonify({
        "status_code": "forbidden_error",
        "message": "Access to this endpoint is forbidden. Only /metrics is allowed."
    }), 403


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom handler for 404 errors.
    """
    return jsonify({
        "status_code": "not_found_error",
        "message": "The requested URL was not found on the server."
    }), 404


@app.route('/metrics', methods=['GET'])
def metrics():
    """
    API endpoint to collect and return system and docker metrics.
    """
    # Collect system data using SystemPlugin
    system_plugin = SystemPlugin()
    system_data = system_plugin.collect_data()

    # Collect Docker data using DockerPlugin
    docker_plugin = DockerPlugin()
    docker_data = docker_plugin.collect_data()

    # Combine both system and docker data
    response_data = {
        "system_metrics": system_data,
        "docker_metrics": docker_data
    }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
