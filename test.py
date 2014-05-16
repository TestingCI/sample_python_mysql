import unittest
from sql import Mysql


class test_db(unittest.TestCase):

    def testRowCount(self):
        mql = Mysql()
        mql.populate()
        self.failIf(mql.rowcount() != 5)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
