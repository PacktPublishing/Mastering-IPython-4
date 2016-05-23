import unittest
from hail1 import f

class TestHailStones(unittest.TestCase):

    def test_f(self):
        ans = [0, 0, 1, 7, 2, 5, 8, 16, 3, 19, 6]
        for i in range(1, 11):
            print(i)
            self.assertEqual(f(i), ans[i])

if __name__ == '__main__':
    unittest.main()
