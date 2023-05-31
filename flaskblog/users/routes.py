from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)    # first arg is name of blueprint

# methods arg allows us to write a list of html requests that our view function could handle 
@users.route('/register', methods=['GET', 'POST'])
def register():
    # check if current is authenticated meaning if the user is logged in we dont want them to see registration or login form again 
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    # check if our form succesfully validated all validations
    if form.validate_on_submit():
        # if form is valid generate hash value for our password...below method returns a byte object and so we decode it into string to then store it in db
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # create a user record in User table class, here we pass in hashed password and not password directly 
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # adding user to our database and commiting the changes
        db.session.add(user)
        db.session.commit()
        # if validated flash method flashes a pop up message as first arg, and second arg is the bootstrap class name we used to style it 
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title="Register", form=form)
    
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        # query the db to make sure the user exists, if exist a user object is returned else it returns None 
        user = User.query.filter_by(email=form.email.data).first()
        # check if user exists and also if it does then check if password matches, first arg is the password hash (as we stored hash value of pswd) and second is password string entered
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # login_user is used to login the user specified and it takes remember as second parameter to decide if u want the user to remember or not
            login_user(user, remember=form.remember.data)
            # Here we will request for next parameter if it exist, args is dict value and using get is better coz if key doesnt exist it will return None
            # if login?next=%2Faccount is in url then next will exist else it wont
            next_page = request.args.get('next')
            # redirect to next_page if next_page exist else redirect to home 
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title="LogIn", form=form)
    
@users.route('/logout')    
def logout():
    # this will logout the user
    logout_user()
    return redirect(url_for('main.home'))

# if user is not logged in first take it to the login page or registration page before viewing the content    
@users.route('/account',  methods=['GET', 'POST'])
@login_required    
def account():
    form = UpdateAccountForm()
    # update the user info
    if form.validate_on_submit():
        # check if form has picture (dp) 
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title="Account", image_file=image_file, form=form)
    
@users.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)   # fetching page - 1 is default page number, type int verifies if page number passed is int
    # search user by username and return the first result we find, if nothing found return 404 http error
    user = User.query.filter_by(username=username).first_or_404()
    # grab only 5 posts per page from the Post table of the specified user only...  \ is used to break line so we could continue or code in next line 
    posts = Post.query.filter_by(author=user)\
            .order_by(Post.date_posted.desc())\
            .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)
    
@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)