from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)   # fetching page - 1 is default page number, type int verifies if page number passed is int
    # grab only 5 posts per page from the Post table
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/about')
def about():
    return render_template('about.html', title="About")

