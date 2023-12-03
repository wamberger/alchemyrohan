

import os
from sqlalchemy import create_engine

import sys
sys.path.append(
    os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    )
)

from alchemyrohan.assemble import assemble_model
from alchemyrohan.utils import is_model
from alchemyrohan.utils import get_model


dir = os.path.dirname(__file__)

conn = "oracle+oracledb://bde:sisbde@tasmania:1521/entw"
table_name = 'ds_col_pref'
import oracledb
oracledb.init_oracle_client(lib_dir=r"C:\oracle\product\instantclient_19_20")

#conn = f"sqlite:///{dir}{os.sep}test_sqlite{os.sep}test.db"
#table_name = 'child'
abs_os_path_to_model = f"{dir}\\test_model"
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

if is_model(table_name, abs_os_path_to_model):
    model = get_model(table_name, py_path_to_model)
    print(f'SqlAlchemy model exist: {model}')
    
    exit(0)

print(f'Something unexpected went wrong')
exit(-1)