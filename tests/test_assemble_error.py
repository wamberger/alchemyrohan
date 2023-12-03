

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


class TestAssembleError(unittest.TestCase):

    @unittest.expectedFailure
    def test_assemble_model_with_error(self):

        dir = os.path.dirname(__file__)
        conn = f"sqlite:///{dir}{os.sep}sqlite{os.sep}test.db"
        table_name = 'parent'
        abs_os_path_to_model = f"{dir}"
        py_path_to_model = 'error.path'

        engine = create_engine(conn)
        assemble_model(
            engine, 
            table_name, 
            abs_os_path_to_model,
            py_path_to_model
            )
        with self.assertRaises(ValueError):
            raise ValueError("This is an expected error")


if __name__ == '__main__':
    unittest.main()