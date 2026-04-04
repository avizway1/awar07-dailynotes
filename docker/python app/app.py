from flask import Flask, jsonify
import os
import sys
import platform
from datetime import datetime

app = Flask(__name__)

# -------------------------------------------------------
# Config from environment variables (good Docker practice)
# -------------------------------------------------------
APP_ENV  = os.environ.get("APP_ENV", "development")
APP_PORT = int(os.environ.get("APP_PORT", 8080))
APP_NAME = os.environ.get("APP_NAME", "Aviz Docker Test App")

# -------------------------------------------------------
# Routes
# -------------------------------------------------------

@app.route("/", methods=["GET"])
def home():
    """Root endpoint — confirms the container is alive."""
    return jsonify({
        "status":    "running",
        "message":   f"Welcome to {APP_NAME}!",
        "env":       APP_ENV,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/health", methods=["GET"])
def health():
    """
    Health-check endpoint.
    Used by Docker HEALTHCHECK, ALB, ECS, K8s liveness probes.
    Always returns 200 if the app is up.
    """
    return jsonify({
        "status": "healthy",
        "uptime": "ok"
    }), 200


@app.route("/info", methods=["GET"])
def info():
    """
    System info endpoint — useful to verify Docker runtime environment.
    Shows Python version, OS, hostname (container ID), env vars.
    """
    return jsonify({
        "app_name":      APP_NAME,
        "environment":   APP_ENV,
        "python_version": sys.version,
        "platform":      platform.platform(),
        "hostname":      platform.node(),          # = container ID in Docker
        "port":          APP_PORT,
        "timestamp":     datetime.utcnow().isoformat() + "Z"
    })


@app.route("/env", methods=["GET"])
def show_env():
    """
    Shows environment variables passed into the container.
    Great for testing --env-file or -e flags with docker run.
    Does NOT expose sensitive values — only APP_* prefixed vars.
    """
    safe_env = {k: v for k, v in os.environ.items() if k.startswith("APP_")}
    return jsonify({
        "environment_variables": safe_env
    })


# -------------------------------------------------------
# Entrypoint
# -------------------------------------------------------
if __name__ == "__main__":
    print(f"[{APP_NAME}] Starting on port {APP_PORT} in '{APP_ENV}' mode...")
    app.run(host="0.0.0.0", port=APP_PORT, debug=(APP_ENV == "development"))