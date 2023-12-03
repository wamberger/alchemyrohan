

import sys
import os
import unittest

sys.path.append(
    os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    )
)

from alchemyrohan.utils import is_model
from alchemyrohan.utils import get_model


class TestAssemble(unittest.TestCase):

    def test_is_model(self):

        dir = os.path.dirname(__file__)
        table_name = 'parent'
        abs_os_path_to_model = os.path.join(dir, 'test_model')

        test_cases = [
            ('parent', True),
            ('child', True)
        ]

        for table_name, expected_result in test_cases:
            result = is_model(
                    table_name, 
                    abs_os_path_to_model
                )
            self.assertEqual(result, expected_result)


    def test_get_model(self):

        from tests.test_model.Parent import Parent
        from tests.test_model.Child import Child

        
        py_path_to_model = 'tests.test_model'
        test_cases = [
            ('parent', Parent)
            ('child', Child)
        ]

        for table_name, expected_result in test_cases:
            result = get_model(
                    table_name, 
                    py_path_to_model
                )
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()