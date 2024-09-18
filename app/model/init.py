from app import db
from typing import TypeVar, Type, Optional
from sqlalchemy_serializer import SerializerMixin

T = TypeVar('T', bound='BaseModel')

class BaseModel(db.Model, SerializerMixin):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP'))
    modified_on = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    @classmethod
    def find(cls: Type[T], id: int) -> Optional[T]:
        return cls.query.get(id)

    def __repr__(self):
        class_name = type(self).__name__
        return f'<{class_name} {self.id}>'