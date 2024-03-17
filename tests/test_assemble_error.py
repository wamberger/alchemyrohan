

import sys
import os
import unittest

sys.path.append(
    os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    )
)

from alchemyrohan.assemble import assemble_models


class TestAssembleError(unittest.TestCase):

    @unittest.expectedFailure
    def test_assemble_model_with_error(self):

        dir = os.path.dirname(__file__)
        db_creds = f"sqlite:///{dir}{os.sep}sqlite{os.sep}test.db"
        table_names = ['parent', 'child']
        abs_os_path_to_model = f"{dir}"
        py_path_to_model = 'error.path'

        assemble_models(
            db_creds, 
            table_names, 
            abs_os_path_to_model,
            py_path_to_model
            )
        with self.assertRaises(ValueError):
            raise ValueError("This is an expected error")


if __name__ == '__main__':
    unittest.main()