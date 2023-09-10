from flask import Flask

def  create_app():
    app = Flask(__name__)
    #encrypt your session and cookies data
    app.config['SECRET_KEY'] = 'sanasaumya'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    
    return app