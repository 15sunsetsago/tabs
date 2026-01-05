from flask import Flask
from .config import Config
from .extensions import db, jwt, migrate, cors

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    from .routes.health import health_bp
    app.register_blueprint(health_bp)

    return app
