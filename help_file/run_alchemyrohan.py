

import os

from sqlalchemy.exc import SQLAlchemyError
from alchemyrohan import assemble_models


def main():

    path = os.path.dirname(__file__)

    # Sqlite example
    conn_str = f"sqlite:///{path}{os.sep}test_sqlite{os.sep}test.db"
    # Oracle-Database example
    # db_creds = f'oracle+oracledb://{username}:{password}@{hostname}:{port}/{service_name}'

    path = os.path.join(path, 'test_models') # path to save models
    py_path = 'tests.test_models' # pythonic path to models

    table_names = ['parent', 'child'] # all names will be capitilized

    try:
        assemble_models(conn_str, table_names, path,py_path)
    except SQLAlchemyError as e:
        raise SQLAlchemyError(e) from e


if __name__ == '__main__':
    main()
