from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = "iam>iwas"
    from app.routes.routes import bp
    
    # Registrar o blueprint
    app.register_blueprint(bp)

    return app

