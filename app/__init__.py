from flask_simplemde import SimpleMDE
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_admin import Admin






login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
admin = Admin()


simple = SimpleMDE()
bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    simple.init_app(app)
   
   
    
    # Registering blog blueprint
    # from .Blog import blog as blog_blueprint
    # app.register_blueprint(blog_blueprint)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # Regestering the auth bluprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Will add the views and forms


    # configure UploadSet
    
    return app