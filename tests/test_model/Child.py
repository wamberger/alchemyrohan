

from sqlalchemy import Column
from tests.test_model import Base
from sqlalchemy.dialects.sqlite import INTEGER
from sqlalchemy.dialects.sqlite import TEXT
from sqlalchemy.orm import relationship


class Child(Base):
    __tablename__ = 'child'


    id = Column(INTEGER, primary_key=True)
    parent_id = Column(INTEGER, nullable=True, default=None)
    name = Column(TEXT, nullable=True, default=None)
    grade = Column(INTEGER, nullable=True, default=None)


    parent_Parent = relationship("Parent", back_populates="children_Child", lazy="joined")

    def __post_init__(self):

        if not isinstance(self.id, int):
            try:
                self.id = int(self.id)
            except:
                raise SyntaxError(f'< {self.id} > is not integer')
        
        if not isinstance(self.parent_id, int):
            try:
                self.parent_id = int(self.parent_id)
            except:
                raise SyntaxError(f'< {self.parent_id} > is not integer')
        
        if not isinstance(self.name, str):
            try:
                self.name = str(self.name)
            except:
                raise SyntaxError(f'< {self.name} > is not string')
        
        if not isinstance(self.grade, int):
            try:
                self.grade = int(self.grade)
            except:
                raise SyntaxError(f'< {self.grade} > is not integer')
        
    
    def __str__(self):

        return f'User(id={self.id},'\
			f'parent_id={self.parent_id},'\
			f'name={self.name},'\
			f'grade={self.grade})'

