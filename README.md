


# Alchemyrohan

![build passing](https://img.shields.io/badge/build-passing-green) ![pypi v22.0.3](https://img.shields.io/badge/pypi-v22.0.3-yellow) ![Python 3.9 | 3.10 | 3.11](https://img.shields.io/badge/python-3.9_|_3.10_|_3.11-blue) ![SqlAlchemy](https://img.shields.io/badge/SqlAlchemy-2.0-red)


Alchemyrohan is an extension package for SqlAlchemy[^1] which automatically creates the database models according to the database schema.
[^1]: [sqlalchemy](https://www.sqlalchemy.org/)


## 🔧 How to Install

With pip package installer from PyPI[^2] directly:
[^2]: [pip](https://pypi.org/project/pip/)

```
pip install alchemyrohan
```

of from source:
```
git clone --recursive https://github.com/wamberger/alchemyrohan.git
cd alchemyrohan
python3 setup.py install
```

## ✏️ How to use

Import in your code:

`import alchemyrohan` 

or 

`import alchemyrohan as ar`

### Functions

- **assemble_model()** is the main function. This function is used to create a SqlAlchemy database model and accepts next arguments:
    | argument | description |
    | --------- | --------- |
    | *engine* | this is SqlAlchemy engine  `from sqlalchemy import create_engine` |
    | *table_name* | this is the name of the database table |
    | *abs_os_path_to_model* | absolute path to the model's folder |
    | *py_path_to_model* | pythonic path to the models |

- **reload_module()** when the code and file are getting created, the python need again to compile the new code. Thus you need to call the reload function. You will need to add pythonic path/import:

`` 
import tests.test_model

...some code...

reload_module(tests.test_model)
``

- **is_model()** this function is used to check if the model was created. You need to pass the <*table_name*> and <*abs_os_path_to_model*> arguments.

- **get_model()** you retrieve the wanted database object of SqlAlchemy model. It needs the <*table_name*> and <*py_path_to_model*> arguments.

- **is_module()** this is optional function if you want to check the pythonic path. It needs <*py_path_to_model*> argument.

### Models

Created SqlAlchemy models can be used as 'normal' SqlAlchemy models, but they have some additional features:
- default values
- parent-child relationships
- <*_post_init_*> method is used as validation
- when 'printing' the string will contain the model/object name and attributes names with their values.

All models are named with the same naming convention as they are in the database with one difference, they are capitalized (python class naming convention).


## 📋 Development and DB-Support

Currently supports SqLite and Oracle Database.

* ***v0.1.0***: writing code and tested with SqLite database  
* ***v0.2.0***: tested with Oracle database
* ***v0.3.0***: added additional functions and bug fixing.


## 📝 Examples

**Simple example**: 
``
import os
from sqlalchemy import create_engine

from alchemyrohan.assemble import assemble_model
from alchemyrohan.utils import is_model
from alchemyrohan.utils import get_model
from alchemyrohan.utils import reload_module

import tests.test_model

dir = os.path.dirname(__file__)
conn = f"sqlite:///{dir}{os.sep}test_sqlite{os.sep}test.db"

engine = create_engine(conn)
table_name = 'child' # all names will be capitilized
abs_os_path_to_model = os.path.join(dir, 'test_model') # path
py_path_to_model = 'tests.test_model' # pythonic path

try:
    assemble_model(
        engine, 
        table_name, 
        abs_os_path_to_model,
        py_path_to_model
        )
except Exception as e:
    print(e)
    exit(1)

reload_module(tests.test_model) # compile the new code

if is_model(table_name, abs_os_path_to_model):
    model = get_model(table_name, py_path_to_model)
    print(f'SqlAlchemy model exist: {model}')
    
    exit(0)

print(f'Something unexpected went wrong')
exit(-1)
``

**Example of a model**:
``

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

``

## ❗ IMPORTANT - Possible Errors!

In some cases you will need to correct the code manually. 
This can be the case when:

- your are creating only one model which has relationship to other tables, thus you will need to create also those models or delete the part of the code.

- your tables have no primary keys. SqlAlchemy needs one primary key.

- your database has some datatypes or features which were not yet been testet.

## 📄 License

Alchemyrohan is MIT licensed, as found in the [LICENSE][1] file.

[1]: https://github.com/wamberger/alchemyrohan/blob/master/LICENSE