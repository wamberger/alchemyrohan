

import sys
import os
import unittest

sys.path.append(
    os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    )
)

from sqlalchemy import create_engine
from alchemyrohan.assemble import assemble_model


class TestAssemble(unittest.TestCase):

    def test_assemble_model_sqlite_db(self):

        dir = os.path.dirname(__file__)
        conn = f"sqlite:///{dir}{os.sep}test_sqlite{os.sep}test.db"
        abs_os_path_to_model = os.path.join(dir, 'test_model')
        py_path_to_model = 'tests.test_model'

        test_cases = [
            'parent',
            'child'
        ]

        for table_name in test_cases:
            try:
                engine = create_engine(conn)

                assemble_model(
                    engine, 
                    table_name, 
                    abs_os_path_to_model,
                    py_path_to_model
                    )
            except Exception as e:
                self.fail(
                    f"Sqlite - Function raised an unexpected exception: {e}")


if __name__ == '__main__':
    unittest.main()
