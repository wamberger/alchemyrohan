


# Alchemyrohan

 ![pypi v22.0.3](https://img.shields.io/badge/pypi-v22.0.3-yellow) ![Python 3.9 | 3.10 | 3.11](https://img.shields.io/badge/python-3.9_|_3.10_|_3.11-blue) ![SqlAlchemy](https://img.shields.io/badge/SqlAlchemy-2.0-red)


Alchemyrohan is a tool for **[SqlAlchemy](https://www.sqlalchemy.org/)** that helps to create database models based on the database schema.

---

## 📖 Content

- [How to Install](#-How-to-Install)
- [Database Support](#-Database-Support)
- [How to use](#-How-to-use)
  - [Functions](#-Functions)
    - [Main Function](#-Main-Function)
    - [Optional Functions](#-Optional-Functions)
  - [Models](#-Models)
- [Example](#-Example)
- [Dependencies](#-Dependencies)
- [Important Note](#Important-Note)
- [Release Notes](#-Release-Notes)
- [License](#-License-and-Third-Party-Licenses)

---


## 🔧 How to Install

With pip package installer from **[PyPI](https://pypi.org/project/pip/)** directly:

```
pip install alchemyrohan
```

or from source:

```
git clone --recursive https://github.com/wamberger/alchemyrohan.git
cd alchemyrohan
python3 setup.py install
```


## 🗄 Database Support

This project is currently designed to work with the following databases:

- **SqLite**
- **Oracle**


## 🔨 How to use

Import in your code:

`import alchemyrohan` 

or 

`import alchemyrohan as ar`


### 🪄 Functions

#### 🔮 Main Function

- **assemble_models()** is the main function. This function is used to create a SqlAlchemy database model and is accepting the following arguments:
    | argument | description |
    | --------- | --------- |
    | *db_creds* | Credential string to connect to the database |
    | *table_names* | Names of the tables |
    | *abs_path_to_models* | Absolute path to the location where the created models will be saved |
    | *py_path_to_model* | pythonic path to the models |


#### 💉 Optional Functions

- **is_model():** This function is used to check if the model exists. You need to pass the *table_name* and *abs_path_to_model* arguments.

- **get_model():** It retrieves the desired database object of the SqlAlchemy model. It requires the *table_name* and *py_path_to_model* arguments.

- **is_module():** This function is used to check the Pythonic path. It requires the *py_path_to_model* argument.

- **reload_module():** If you have a specific reason for using the code in production or creating models in a running script, you may need to compile the newly created code. In such cases, you will need to use this function. Here's how you do it:

    ~~~python
    import tests.test_models

    ...some code...

    reload_module(tests.test_models)
    ~~~

### 🗂 Models

Created SqlAlchemy models have some additional features:

- Default values.
- Parent-child relationships.
- The *_post_init_* method is used for validation.
- When 'printing', the string will contain the model/object name and attribute names with their values.

All models are named with the same convention as they are in the database, with one difference: they are capitalized according to Python class naming conventions.


## 📝 Example

**Simple example how to use the code:**

~~~python

import os

from alchemyrohan.assemble import assemble_models

dir = os.path.dirname(__file__)

# Sqlite example
db_creds = f"sqlite:///{dir}{os.sep}test_sqlite{os.sep}test.db"
# Oracle-Database example
#db_creds = f'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{service_name}'

abs_os_path_to_model = os.path.join(dir, 'test_models') # path to save models
py_path_to_model = 'tests.test_models' # pythonic path to models
table_names = ['parent', 'child'] # all names will be capitilized

try:
    assemble_models(
        db_creds, 
        table_names, 
        abs_path_to_models,
        py_path_to_model
        )
    exit(0)
except Exception as e:
    print(e)
    exit(1)

~~~

**Example of one created model**:

~~~python

from sqlalchemy import Column
from tests.test_models import Base
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

~~~ 


## 📚 Dependencies

- **sqlalchemy** (version 2.0.x) is an ORM and provides code for its models.
- **oracledb** (version 1.4.x) is used to shape a database table model with an Oracle table schema.


## ❗Important Note

In most cases, you will need to correct the code manually. 
This will be the case when:

- You are not adding a Pythonic path.

- You are creating only one model which has relationships to other tables, thus you will need to create those models or delete the relevant part of the code.

- Your tables have no primary keys. SQLAlchemy requires at least one primary key.

- Your database may have some data types or features which have not yet been tested.


## 📋 Release Notes


- ***v0.1.0*** - creation of the initial code and tested with SqLite database
- ***v0.2.0*** - tested with Oracle database
- ***v0.3.0*** - added additional functions
- ***v0.3.1*** - bug fixing
- ***v0.3.2*** - text fixing and adding third party licenses
- ***v0.4.0*** - Main update! Not compatible with previous versions. Changes:
    - Changed function name from *assemble_model()* to *assemble_models()*.
    - Updated parameters of the *assemble_models()* function.
    - Revised code structure of the *assemble_models()* function.
    - Adjusted naming or added text in *utils.py*, *wizard.py* and *__init__py*.
    - Updated README.md file.


## 📄 License and Third-Party Licenses

Alchemyrohan is MIT licensed, as stated in the [LICENSE][1] file.

The following software components are included in this project:

* SqlAlchemy (MIT License)
* python-oracledb (Apache License 2.0) 

[THIRD PARTY LICENSES][2]


[1]: https://github.com/wamberger/alchemyrohan/blob/master/LICENSE
[2]: https://github.com/wamberger/alchemyrohan/blob/master/THIRD_PARTY_LICENSES