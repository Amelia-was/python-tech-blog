from app.db import Base
from sqlalchemy import Column, Table, String, Integer, ForeignKey

# association_table = Table('association', Base.metadata,
#     Column('id', Integer, primary_key=True),
#     Column('post_id', Integer, ForeignKey('posts.id')),
#     Column('tag_name', String(20), ForeignKey('tags.name'))
# )

class Tag(Base):
    __tablename__ = 'tags'
    name = Column(String(20), primary_key=True)