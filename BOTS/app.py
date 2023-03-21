from flask import Flask

def create_app():
    app = Flask(__name__)
    # здесь можно добавить конфигурацию приложения, регистрацию Blueprint-ов, и т.д.
    return app
