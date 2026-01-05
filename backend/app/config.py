import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "tabs-dev-secret")
    SQLALCHEMY_DATABASE_URI = "sqlite:///tabs.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "tabs-jwt-secret")
