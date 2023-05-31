# Flask Blog

Flask Blog is a web application built with Python using the Flask framework. It provides a platform for users to create, read, update, and delete blog posts. The application also includes user management functionalities such as user registration, login, logout, password reset, and user profile management.


## Features

#### Blog Post Management

- Create a new blog post by providing a title, content, and optional image.
- Allows you to edit or delete your existing blog post.
- View other people's blog posts

#### User Management

- Register a new user account by providing a unique username, valid email address, and secure password.
- Log in to an existing user account using the email and password.
- Log out from the user account, ending the session.
- Reset the password by requesting a password reset email.
- Update the user profile information, including the username, email, and profile image.
- Delete the user account, removing all associated blog posts.

#### Authentication and Authorization

Secure user authentication using password hashing with bcrypt.
Protect routes and functionalities from unauthorized access.
Restrict access to certain actions based on user roles or ownership.

## Prerequisites

- Python 3.6 or higher
- External dependencies (specified in the **requirements.txt** file)

## Installation

To run the Flask Blog application locally, please follow the steps below:
1.  Clone the repository:

```shell
    git clone <repository-url>
```

2.  Navigate to the project directory:

```shell
    cd BlogIt
```

3.  Create and activate a virtual environment:

```shell
    python -m venv venv
```
        For Windows:

```shell
```
    venv\Scripts\activate
        For macOS/Linux:

```shell
    source venv/bin/activate
```

4.   Install the required dependencies:

```shell
    pip install -r requirements.txt
```

5.   Make necessary changes to **config.py** file:

    To generate a secret key, run below script
```shell
    import secrets
	   your_secret_key = secrets.token_hex(16)
```
 
    Copy the output and assign it to SECRET_KEY varible
```shell
	   SECRET_KEY = your_secret_key
```	
	
	Provide your DB URI if u already have one. Else to use existing DB:
```shell
	   SQLALCHEMY_DATABASE_URI = sqlite:///site.db
```	
    
	Use your working email and password - this is used to as source email for sending mails
    
```shell	
	   MAIL_USERNAME = [your_email]
    MAIL_PASSWORD = [your_password]
```

6.  Now, run the flask server:
```shell
    python run.py
```	 

7.   Visit the site on the localhost:[port] as specified by the server.


## Dependencies

The Flask Blog application utilizes the following external modules:

			alembic==1.7.7
			bcrypt==3.2.2
			blinker==1.4
			cffi==1.15.0
			click==8.1.3
			colorama==0.4.4
			dnspython==2.2.1
			dominate==2.6.0
			email-validator==1.2.1
			Flask==2.1.2
			Flask-Bcrypt==1.0.1
			Flask-Bootstrap==3.3.7.1
			Flask-Login==0.6.1
			Flask-Mail==0.9.1
			Flask-Migrate==3.1.0
			Flask-Moment==1.0.2
			flask-mongoengine==1.0.0
			Flask-SQLAlchemy==2.5.1
			Flask-WTF==1.0.1
			idna==3.3
			importlib-metadata==4.11.3
			importlib-resources==5.7.1
			itsdangerous==2.0.0
			Jinja2==3.1.2
			Mako==1.2.0
			MarkupSafe==2.1.1
			mongoengine==0.24.1
			mysql-connector-python==8.0.29
			Pillow==9.1.0
			protobuf==3.20.1
			pycparser==2.21
			PyJWT==2.3.0
			pymongo==4.1.1
			PyMySQL==1.0.2
			SQLAlchemy==1.4.36
			typing_extensions==4.2.0
			visitor==0.1.3
			Werkzeug==2.1.2
			WTForms==3.0.1
			zipp==3.8.0 




## File Structure

The project consists of the following files:
```shell
README.md
run.py
flaskblog
│
│   config.py
│   models.py
│   site.db
│   __init__.py
│
├───errors
│   │   handlers.py
│   │   __init__.py
│   │
│   └───__pycache__
│           handlers.cpython-37.pyc
│           __init__.cpython-37.pyc
│
├───main
│   │   routes.py
│   │   __init__.py
│   │
│   └───__pycache__
│           routes.cpython-37.pyc
│           __init__.cpython-37.pyc
│
├───posts
│   │   forms.py
│   │   routes.py
│   │   __init__.py
│   │
│   └───__pycache__
│           forms.cpython-37.pyc
│           routes.cpython-37.pyc
│           __init__.cpython-37.pyc
│
├───static
│   │   main.css
│   │
│   └───profile_pics
│           0b01c716476c27fc.jpg
│           415573be5a30e82e.jpg
│           d6a978033a14bfe6.jpg
│           default.jpg
│
├───templates
│   │   about.html
│   │   account.html
│   │   create_post.html
│   │   home.html
│   │   layout.html
│   │   login.html
│   │   post.html
│   │   register.html
│   │   reset_request.html
│   │   reset_token.html
│   │   user_posts.html
│   │
│   └───errors
│           403.html
│           404.html
│           500.html
│
├───users
│   │   forms.py
│   │   routes.py
│   │   utils.py
│   │   __init__.py
│   │
│   └───__pycache__
│           forms.cpython-37.pyc
│           routes.cpython-37.pyc
│           utils.cpython-37.pyc
│           __init__.cpython-37.pyc
│
└───__pycache__
        config.cpython-37.pyc
        models.cpython-37.pyc
        __init__.cpython-37.pyc
```

## Contributing

Contributions to the flask blog application are highly appreciated! If you find any issues, have suggestions for improvements, or would like to add new features, please consider contributing. To contribute, you can follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the main branch to work on your changes.
3. Make the necessary modifications and improvements to the codebase.
4. Write tests to ensure the stability and correctness of your changes.
5. Commit your changes and push them to your forked repository.
6. Open a pull request against the main repository, describing your changes in detail.

Please ensure that your contributions align with the following guidelines:

- Follow the existing coding style and conventions used in the project.
- Write clear and concise commit messages and provide an informative description in your pull request.
- Test your changes thoroughly and ensure they do not introduce any regressions.
- Provide proper documentation and comments to help others understand your contributions.

By contributing to the flask blog application, you'll be helping to improve its functionality, stability, and user experience for everyone. Thank you for your contributions in advance!.