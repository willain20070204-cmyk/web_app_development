from flask import Flask
from .dashboard_routes import dashboard_bp
from .book_routes import book_bp
from .member_routes import member_bp
from .record_routes import record_bp

def register_blueprints(app: Flask):
    """
    註冊所有的 Blueprint 到 Flask App
    """
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(member_bp)
    app.register_blueprint(record_bp)
