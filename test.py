
import unittest
from dots import Dot, DotCollection

class DotTest(unittest.TestCase):
    def test_x_and_y_set(self):
        dot = Dot(1, 2)
        self.assertEqual(1, dot.x)
        self.assertEqual(2, dot.y)


class DotCollectionTest(unittest.TestCase):
    def test_set(self):
        dot_collection = DotCollection([Dot(1,2)])
        self.assertEqual(1, dot_collection.dots[0].x)
        self.assertEqual(2, dot_collection.dots[0].y)

    def test_is_on_same_line(self):
        # no dots is not a line
        dot_collection = DotCollection([])
        self.assertFalse(dot_collection.is_on_same_line())

        # 1 dot is not a line
        dot_collection = DotCollection([Dot(1,2)])
        self.assertFalse(dot_collection.is_on_same_line())

        # 2 dots
        dot_collection = DotCollection([Dot(1,2), Dot(1,3)])
        self.assertTrue(dot_collection.is_on_same_line())

        # 3 linear dots (1x + 1 = y)
        dot_collection = DotCollection([Dot(1,2), Dot(2,3), Dot(3,4)])
        self.assertTrue(dot_collection.is_on_same_line())

        # 3 linear dots (x = y)
        dot_collection = DotCollection([Dot(1,1), Dot(3,3), Dot(4,4)])
        self.assertTrue(dot_collection.is_on_same_line())

        # 3 linear dots (y = 1)
        dot_collection = DotCollection([Dot(1,1), Dot(3,1), Dot(4,1)])
        self.assertTrue(dot_collection.is_on_same_line())

        # 3 linear dots (x=1)
        dot_collection = DotCollection([Dot(1,5), Dot(1,10), Dot(1,20)])
        self.assertTrue(dot_collection.is_on_same_line())

        # 3 non-linear dots
        dot_collection = DotCollection([Dot(1,2), Dot(5,3), Dot(1,4)])
        self.assertFalse(dot_collection.is_on_same_line())


if __name__ == '__main__':
    unittest.main()
