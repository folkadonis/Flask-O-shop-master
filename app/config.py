import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_USERNAME = os.environ.get("EMAIL")
    MAIL_PASSWORD = os.environ.get("PASSWORD")
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_USE_TLS = True
    MAIL_PORT = 587
    STRIPE_PRIVATE_KEY = os.environ.get("STRIPE_PRIVATE")
    ENDPOINT_SECRET = os.environ.get("ENDPOINT_SECRET")
