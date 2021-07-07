from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func, PickleType
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.ext.mutable import MutableList

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    body = Column(String(5000), nullable=False)
    tags = Column(MutableList.as_mutable(PickleType), default=[])
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User')
    comments = relationship('Comment', cascade='all,delete')