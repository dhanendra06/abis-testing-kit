import unittest
from src.config import CBEFFConfig
from typing import List, AnyStr


class MyTestCase(unittest.TestCase):

    def test_something(self):
        list_of_biometrics: List = []
        from src.cbeff import Biometrics, create
        b1: Biometrics = Biometrics('IRIS', 'Left Eye', 'fdfdfdfdgdg')
        list_of_biometrics.append(b1)
        create(list_of_biometrics, './tmp_data/test1.xml')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
