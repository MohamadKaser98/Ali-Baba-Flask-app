from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SLGDFMKADSF ASDQEWTY DFMLK'

    from .views import views
    from .auth import auth
    from .admin import admin
    
    app.register_blueprint(views, url_prefix='/') # go to localhost:5000/about-us (for example)
    app.register_blueprint(auth, url_prefix='/auth') #go to localhost:5000/auth/login (for example)
    app.register_blueprint(admin, url_prefix='/')

    return app