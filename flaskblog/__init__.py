from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config



# creating instance
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()   # this is used to handle user sessions for us
# here the value passed is the name of our view function
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'   # info is class name in bootstrap to provide a good css

# creating mail instance
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    # we are configuring our app using an object of Config class and so we used from_object
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # its imported here to avoid circular import conflicts
    # importing instance of blueprints
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    # register blueprints to use it 
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    return app