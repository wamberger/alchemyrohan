

from sqlalchemy import Column
from tests.test_model import Base
from sqlalchemy.dialects.sqlite import INTEGER
from sqlalchemy.dialects.sqlite import TEXT
from sqlalchemy.dialects.sqlite import REAL
from sqlalchemy.dialects.sqlite import BLOB


class Parent(Base):
    __tablename__ = 'parent'


    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=True, default=None)
    age = Column(INTEGER, nullable=True, default=None)
    height = Column(REAL, nullable=True, default=None)
    is_active = Column(BLOB, nullable=True, default=None)



    def __post_init__(self):

        if not isinstance(self.id, int):
            try:
                self.id = int(self.id)
            except:
                raise SyntaxError(f'< {self.id} > is not integer')
        
        if not isinstance(self.name, str):
            try:
                self.name = str(self.name)
            except:
                raise SyntaxError(f'< {self.name} > is not string')
        
        if not isinstance(self.age, int):
            try:
                self.age = int(self.age)
            except:
                raise SyntaxError(f'< {self.age} > is not integer')
        
        if not isinstance(self.height, float):
            try:
                self.height = float(self.height)
            except:
                raise SyntaxError(f'< {self.height} > is not float')
        
        if not isinstance(self.is_active, str):
            try:
                self.is_active = str(self.is_active)
            except:
                raise SyntaxError(f'< {self.is_active} > is not string')
        
    
    def __str__(self):

        return f'User(id={self.id},'\
			f'name={self.name},'\
			f'age={self.age},'\
			f'height={self.height},'\
			f'is_active={self.is_active})'

