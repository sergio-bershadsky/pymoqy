import unittest
from pymoqy.node import Node


class TestNode(unittest.TestCase):

    def test_and(self):
        n1 = Node(1)
        n2 = Node(2)
        q = (n1 & n2).data
        self.assertDictEqual({'$and': [1, 2]}, q)

    def test_or(self):
        n1 = Node(1)
        n2 = Node(2)
        q = (n1 | n2).data
        self.assertDictEqual({'$or': [1, 2]}, q)

    def test_invert(self):
        n1 = Node(1)
        q = (~n1).data
        self.assertDictEqual({'$not': 1}, q)

    def test_complex_1(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        q = (n1 | n2 & n3 | n4).data
        self.assertDictEqual({'$or': [1, {'$and': [2, 3]}, 4]}, q)

    def test_complex_2(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        q = ((n1 | n2) & (n3 | n4)).data
        self.assertDictEqual({'$and': [{'$or': [1, 2]}, {'$or': [3, 4]}]}, q)

    def test_complex_3(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        q = (n1 | ((n2 & n3) | n4)).data
        self.assertDictEqual({'$or': [1, {'$or': [{'$and': [2, 3]}, 4]}]}, q)

    def test_reuse(self):
        n1 = Node(1)
        n2 = Node(2)
        q = (n1 & n2).data
        self.assertDictEqual({'$and': [1, 2]}, q)
        q = (n1 | n2 & n1).data
        self.assertDictEqual({'$or': [1, {'$and': [2, 1]}]}, q)

    def test_reuse_2(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = n1 | n2
        n4 = n3 & n1
        q1 = (n1 & n2 | n3 & n4).data
        q2 = (n1 & n2 | (n1 | n2) & ((n1 | n2) & n1)).data
        self.assertDictEqual(q1, q2)

    def test_nor(self):
        """
        Python does not have nor operator but mongo does not have xor operator
        So i decided to use ^ (XOR) python operator as NOR operator for mongo
        """
        n1 = Node(1)
        n2 = Node(2)
        q = (n1 ^ n2).data
        self.assertDictEqual(q, {'$nor': [1, 2]})

if __name__ == '__main__':
    unittest.main()