from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    # get all posts
    #
    return (render_template(
        'homepage.html'
    ))

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
    # get single post by id
    #
    return render_template(
        'single-post.html'
    )

@bp.route('/user/<id>')
def single_user(id):
    # get single user by id
    #
    return render_template(
        'single-user.html'
    )