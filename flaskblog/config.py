import os

class Config:
    # secrets is an inbuilt module which is used to generate random large numbers or keys directly for us...
    # secret keys protects against modifying cookies and cross-site forgery attacks and things like that. We set this value to config file using app.config()
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # setting our sqlalchemy db uri to sqlite3... /// means current dir path so site.db will be created in current dir 
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # setting up config for our email service
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # storing email and passwords to envrionment variable so as to not expose it publicly through code to others
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    