from app.db import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class PostTag(Base):
    __tablename__ = 'post_tags'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    tag_name = Column(String(20), ForeignKey('tags.name'))