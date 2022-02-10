from flask import Blueprint, render_template, session, redirect
from app.models import User, Post, Tag
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    # get all posts
    db = get_db()
    posts = db.query(Post).order_by(Post.created_at.desc()).all()

    return render_template(
        'homepage.html',
        posts=posts,
        loggedIn=session.get('loggedIn')
    )

@bp.route('/tagged/<tag>')
def tagged(tag):
    # get all posts tagged <tag>
    db = get_db()
    posts = db.query(Tag).filter(Tag.tag_name == tag).all()

    return render_template(
        'homepage.html',
        posts=posts,
        loggedIn=session.get('loggedIn')
    )

@bp.route('/tags')
def all_tags():
    # get all posts tagged <tag>
    db = get_db()
    posts = db.query(Tag).all()

    return render_template(
        'homepage.html',
        posts=posts,
        loggedIn=session.get('loggedIn')
    )

@bp.route('/login')
def login():
    if session.get('loggedIn') is None:
        return render_template('login.html')
    return redirect('/dashboard')

@bp.route('/post/<id>')
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    return render_template(
        'single-post.html',
        post=post,
        loggedIn=session.get('loggedIn')
    )

@bp.route('/user/<id>')
def single_user(id):
    # get single user by id
    db = get_db()
    user = db.query(User).filter(User.id == id).one()
    posts = db.query(Post).filter(Post.user_id == id).order_by(Post.created_at.desc()).all()

    return render_template(
        'single-user.html',
        user=user,
        posts=posts
    )