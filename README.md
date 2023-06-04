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

### News
Flask blog displays news on the sidebar, which helps stay up-to-date with outside world.


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
    venv\Scripts\activate
```        
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

6.  Get a new api key from newsapi.org and paste it in place of **NEWS_API_KEY** inside **news.py** file
```shell	
    newsapi = NewsApiClient(api_key=YOUR_API_KEY)
```

7.   Now, run the flask server:
```shell
    python run.py
```	 

8.   Visit the site on the localhost:[port] as specified by the server.


## Dependencies

The Flask Blog application utilizes the following external modules:

	alembic==1.7.7
	bcrypt==3.2.2
	blinker==1.4
	certifi==2023.5.7
	cffi==1.15.0
	charset-normalizer==3.1.0
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
	newsapi-python==0.2.7
	Pillow==9.1.0
	protobuf==3.20.1
	pycparser==2.21
	PyJWT==2.3.0
	pymongo==4.1.1
	PyMySQL==1.0.2
	requests==2.31.0
	SQLAlchemy==1.4.36
	typing_extensions==4.2.0
	urllib3==2.0.2
	visitor==0.1.3
	Werkzeug==2.1.2
	WTForms==3.0.1
	zipp==3.8.0




## File Structure

The project consists of the following files:
```shell
README.md
news.py
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


## Technologies Used

- Python
- Flask
- HTML
- CSS
- Bootstrap
- Jinja2


## Design and Architecture

BlogIt follows a scalable and maintainable architecture. The application is designed using the Model-View-Controller (MVC) pattern, separating the data model, business logic, and user interface. This separation allows for easy modification and extension of different components without impacting others. The application leverages Flask's modular structure to organize routes, forms, templates, and static files into separate directories, promoting code organization and reusability.

The database is managed using SQLAlchemy, an Object-Relational Mapping (ORM) library for Python. SQLAlchemy provides a high-level interface for interacting with the database, allowing for efficient data retrieval, modification, and querying. The database schema is defined using SQLAlchemy's declarative syntax, making it easy to define models and their relationships.

The user interface is built using Flask's integrated templating engine, Jinja2. Templates are used to generate dynamic HTML pages by combining static HTML with Python code. Flask's template inheritance feature enables the reuse of common elements across multiple pages, ensuring consistent styling and layout throughout the application.

To enhance the user experience, Flask Blog incorporates Bootstrap, a popular front-end framework. Bootstrap provides a responsive grid system, pre-styled components, and CSS classes that streamline the design process. By leveraging Bootstrap, the application achieves a clean and modern look while ensuring cross-browser compatibility and mobile responsiveness


## Deployment

BlogIt is currently deployed on **PythonAnywhere**, a popular Python web hosting service. It is hosted securely and accessible to users. The deployment process involves the following steps:

1. Sign up for an account on PythonAnywhere if you haven't already.
2. Create a new web app on PythonAnywhere and select the appropriate Python version.
3. Clone your Flask Blog repository from your version control system (e.g., GitHub) to your PythonAnywhere account.
4. Set up a virtual environment on PythonAnywhere and install the required dependencies by running `pip install -r requirements.txt` in the project directory.
5. Configure the necessary environment variables on PythonAnywhere. This includes setting up the database connection details, secret key, and email credentials for the password reset functionality. You can use the PythonAnywhere web interface or define them in a `.env` file.
6. Set the WSGI file to point to the correct Flask application instance. This typically involves specifying the `app` variable in the WSGI file.
7. Run database migrations on PythonAnywhere using Alembic or the necessary database migration tool. This ensures that the database schema is up to date.
8. Start the Flask application on PythonAnywhere by running the appropriate command, such as `python run.py`, in the project directory. You can specify the host and port configuration if needed.
9. Monitor the PythonAnywhere logs and address any potential issues or errors.

PythonAnywhere provides an easy-to-use web interface and detailed documentation to guide you through the deployment process. Make sure to consult the PythonAnywhere documentation for specific instructions on deploying a Flask application.

## Issues

My current issue is an **SMTP error in the "Forgot Password"** section. When a user requests a password reset email, the application encounters an SMTP error. I am actively investigating and working towards resolving this issue. Any assistance, suggestions, or insights regarding this issue would be greatly appreciated.

If you encounter any other issues or have suggestions for improvement, please feel free to open an issue on the GitHub repository. Your feedback is valuable in making the Flask Blog application better and more robust.

## Acknowledgments

I would like to express my gratitude to the following individuals/resources for their contributions, inspiration, and guidance throughout the development process:

- *Corey Schafer*

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