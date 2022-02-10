from app.models import User, Post, Comment, Tag, PostTag
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
    User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
    User(username='jwilloughway1',
         email='rmebes1@sogou.com', password='password123'),
    User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
    User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
    User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

db.commit()

# create Tags
# html = Tag(name='html'),
# css = Tag(name='css'),
# react = Tag(name='react'),
# oop = Tag(name='oop'),
# javascript = Tag(name='javascript'),
# python = Tag(name='python'),
# productivity = Tag(name='productivity')

# insert tags
# db.add_all([html, css, react, oop, javascript, python, productivity])

# insert tags
db.add_all([
    Tag(name='html'),
    Tag(name='css'),
    Tag(name='react'),
    Tag(name='oop'),
    Tag(name='javascript'),
    Tag(name='python'),
    Tag(name='productivity')
])

db.commit()

# insert posts
# db.add_all([
#     Post(title='Donec posuere metus vitae ipsum', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', post_tags=[css, javascript], user_id=1),
#     Post(title='Morbi non quam nec dui luctus rutrum', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', post_tags=[javascript, python, oop], user_id=1),
#     Post(title='Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', post_tags=[productivity], user_id=2),
#     Post(title='Nunc purus', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', post_tags=[css, html], user_id=3),
#     Post(title='Pellentesque eget nunc', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', post_tags=[react, css], user_id=4)
# ])


# insert posts
db.add_all([
    Post(title='Donec posuere metus vitae ipsum', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', user_id=1),
    Post(title='Morbi non quam nec dui luctus rutrum', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', user_id=1),
    Post(title='Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', user_id=2),
    Post(title='Nunc purus', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', user_id=3),
    Post(title='Pellentesque eget nunc', body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum viverra vitae massa sed tincidunt. Donec facilisis consectetur dolor. Suspendisse fringilla mauris quam, a bibendum arcu venenatis id. Vestibulum ornare orci felis, nec porttitor ante condimentum accumsan. Aliquam non dictum erat, in mattis orci. Aliquam ornare semper ipsum, eu ornare ligula ullamcorper ut.', user_id=4)
])

db.commit()

# insert post_tags
db.add_all([
    PostTag(post_id='1', tag_name='css'),
    PostTag(post_id='1', tag_name='javascript'),
    PostTag(post_id='2', tag_name='javascript'),
    PostTag(post_id='2', tag_name='python'),
    PostTag(post_id='2', tag_name='oop'),
    PostTag(post_id='3', tag_name='productivity'),
    PostTag(post_id='4', tag_name='css'),
    PostTag(post_id='4', tag_name='html'),
    PostTag(post_id='5', tag_name='css'),
    PostTag(post_id='1', tag_name='react'),
])

db.commit()

# insert comments
db.add_all([
    Comment(comment_text='Nunc rhoncus dui vel sem.', user_id=1, post_id=2),
    Comment(comment_text='Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', user_id=1, post_id=3),
    Comment(comment_text='Aliquam erat volutpat. In congue.', user_id=2, post_id=1),
    Comment(comment_text='Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.', user_id=2, post_id=3),
    Comment(comment_text='In hac habitasse platea dictumst.', user_id=3, post_id=3)
])

db.commit()

db.close()

# insert tags
# db.add_all([
#     Tag(tag_name='html', posts=[4]),
#     Tag(tag_name='css', posts=[1, 4, 5]),
#     Tag(tag_name='react', posts=[5]),
#     Tag(tag_name='oop', posts=[2]),
#     Tag(tag_name='javascript', posts=[1, 2]),
#     Tag(tag_name='python', posts=[2]),
#     Tag(tag_name='productivity', posts=[3])
# ])

