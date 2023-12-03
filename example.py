

import os
from sqlalchemy import create_engine
from alchemyrohan.assemble import assemble_model
from alchemyrohan.utils import is_model
from alchemyrohan.utils import get_model
from alchemyrohan.utils import reload_module

dir = os.path.dirname(__file__)

conn = f"sqlite:///{dir}{os.sep}test_sqlite{os.sep}test.db"

table_name = 'child'
abs_os_path_to_model = os.path.join(dir, 'test_model')

import tests.test_model
py_path_to_model = 'tests.test_model'

engine = create_engine(conn)

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

import tests.test_model

reload_module(tests.test_model)

if is_model(table_name, abs_os_path_to_model):
    model = get_model(table_name, py_path_to_model)
    print(f'SqlAlchemy model exist: {model}')
    
    exit(0)

print(f'Something unexpected went wrong')
exit(-1)