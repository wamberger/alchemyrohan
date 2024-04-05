

__all__ = ['assemble_models']

import os

from typing import Iterable
from sqlalchemy import create_engine
from sqlalchemy import Engine
from alchemyrohan.meta_data import MetaDataHolder
from alchemyrohan.wizard import *


def assemble_models(
        conn_str: str,
        table_names: Iterable[str],
        abs_path_to_models: str = '',
        py_path_to_model: str = 'py_path_to_model') -> None:
    """Creates database models for SqlAlchemy.

    Args:
        conn_str (str): Connection string to connect to the database.
        table_names (List[str]): Names of the tables from database.
        abs_path_to_models (str, optional): Absolute path to the location
                                            where the created models will
                                            be saved. Defaults to the
                                            current directory.
        py_path_to_model (str, optional): Pythonic path to the models in
                                          the project. For example,
                                          'project_name.db.models'. This will
                                          be written in code as:
                    'from project_name.db.models.TableName import TableName'.
    Raises:
        Exception: if the 'abs_path_to_models' does not exist.
    """

    if not abs_path_to_models:
        abs_path_to_models = os.getcwd()
    elif not os.path.isdir(abs_path_to_models):
        raise Exception(f'This path does not exist: {abs_path_to_models}')
    
    engine: Engine = create_engine(conn_str)
    for table in table_names:
        code_holder = generate_code(
            MetaDataHolder(engine, table), py_path_to_model)

        model_template = construct_model(code_holder)

        generate_model(table, model_template, abs_path_to_models)

        generate_init_file(table, abs_path_to_models, py_path_to_model)





    