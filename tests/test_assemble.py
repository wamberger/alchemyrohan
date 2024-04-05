

import sys
import os
import unittest


sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(__file__)),))

from alchemyrohan.assemble import assemble_models


class TestAssemble(unittest.TestCase):

    def test_assemble_model_sqlite_db(self):

        dir = os.path.dirname(__file__)
        db_creds = f"sqlite:///{dir}{os.sep}test_sqlite{os.sep}test.db"
        abs_path_to_models = os.path.join(dir, 'test_models')
        py_path_to_models = 'tests.test_models'

        table_names = [
            'parent',
            'child'
        ]

        try:
            assemble_models(
                db_creds, 
                table_names, 
                abs_path_to_models,
                py_path_to_models
                )
        except Exception as e:
            self.fail(
                f"Sqlite - Function raised an unexpected exception: {e}")


if __name__ == '__main__':
    unittest.main()
