

# Alchemyrohan 

Alchemyrohan is an extension package for SqlAlchemy[^1] where the python code of the database models is created automatically according to the database schema.
[^1]: [sqlalchemy](https://www.sqlalchemy.org/)


# How to Install

### Requirements

You will need Python version 3.10.0 or later and pip package installer.[^2]
[^2]: [pip](https://pypi.org/project/pip/)

### Install

The package is currently not available on the PyPi.
Therefore, you can download the tar.gz file from < dist > folder. Then navigate to the file and enter this code in terminal:  

`Python3 pip install ./alchemyrohan-1.0.0.tar.gz`

How to import in your code:

`import alchemyrohan` 

or 

`import alchemyrohan as ar`


# How to use it

There are few main functions which you need to use:

- < assemble_model > is the main function. This function is used to create a SqlAlchemy database model.

- < reload_module > when the code and file are getting created, the python need again to compile the new code. Thus you need to call the reload function.

- < is_model > this function is used to check if the model was created. 

- < get_model > you retrieve the wanted database object of SqlAlchemy model.


# Example

The example code below is simple 

```
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
```


