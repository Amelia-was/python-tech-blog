import sys
from flask import Blueprint, request, jsonify, session
from app.models import User, Post, Comment, Tag, PostTag
from app.db import get_db
from app.utils.auth import login_required

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()
    
    try:
        # create new User object
        newUser = User(
            username = data['username'],
            email = data['email'],
            password = data['password']
        )

        # add user to db
        db.add(newUser)
        db.commit()
    except:
        # insert failed, send error
        print(sys.exc_info()[0])

        # insert failed, so rollback and send error to front end
        db.rollback()
        return jsonify(message = 'Signup failed'), 500

    # clear existing session data and create new session properties (user_id and loggedIn)
    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True

    return jsonify(id = newUser.id)

@bp.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db()

    try:
        user = db.query(User).filter(User.email == data['email']).one()
    except:
        print(sys.exc_info()[0])
        return jsonify(message = 'Incorrect credentials'), 400
    
    if user.verify_password(data['password']) == False:
        return jsonify(message = 'Incorrect credentials'), 400

    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True
    
    return jsonify(id=user.id)

@bp.route('/users/logout', methods=['POST'])
def logout():
    # remove session variables
    session.clear()
    return '', 204

@bp.route('/comments', methods=['POST'])
@login_required
def comment():
    data = request.get_json()
    db = get_db()

    try:
        # create a new comment
        newComment = Comment(
            comment_text = data['comment_text'],
            post_id = data['post_id'],
            user_id = session.get('user_id')
        )

        db.add(newComment)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Comment failed'), 500
    
    return jsonify(id = newComment.id)

@bp.route('/posts', methods=['POST'])
@login_required
def create():
    data = request.get_json()
    db = get_db()

    print(data)

    try:
        # create a new post
        newPost = Post(
            title=data['title'],
            body=data['body'],
            user_id=session.get('user_id')
        )

        db.add(newPost)
        db.commit()
        
        # if there are tags, add PostTags
        if data['tagged']: 
            for tag in data['tagged']:
                newPostTag = PostTag(
                    post_id=newPost.id,
                    tag_name=tag
                )
            db.add(newPostTag)
            db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message='Post failed'), 500

    return jsonify(id=newPost.id)

@bp.route('/posts/<id>', methods=['PUT'])
@login_required
def update(id):
    data = request.get_json()
    db = get_db()

    try:
        # retrive post and update title property
        post = db.query(Post).filter(Post.id == id).one()
        post.title = data['title']
        post.body = data['body']
        db.commit()
    except:
        print(sys.exec_info()[0])

        db.rollback()
        return jsonify(message= 'Post not found'), 404
    
    return '', 204

@bp.route('/posts/<id>', methods=['DELETE'])
@login_required
def delete(id):
    db = get_db()

    try:
        # delete post from db
        db.delete(db.query(Post).filter(Post.id == id).one())
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message='Post not found'), 404

    return '', 204

@bp.route('/tags', methods=['POST'])
@login_required
def create_tag():
    data = request.get_json()
    db = get_db()

    try:
        # create a new post
        newTag = Tag(
            name=data['tagName']
        )

        db.add(newTag)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message='Tag failed'), 500

    return jsonify(name=newTag.name)

@bp.route('/post-tags', methods=['POST'])
@login_required
def create_post_tag():
    data = request.get_json()
    db = get_db()

    try:
        # create a new post
        newPostTag = PostTag(
            post_id=data['post_id'],
            tag_name=data['tag_name']
        )

        db.add(newPostTag)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message='Tag failed'), 500

    return jsonify(id=newPostTag.id)
    
