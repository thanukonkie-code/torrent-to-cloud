from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024

    from .routes import register_routes
    register_routes(app)
    return app
