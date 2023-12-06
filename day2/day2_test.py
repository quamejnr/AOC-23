import unittest
from day2 import cube_conundrum_a, cube_conundrum_b



class Day2Test(unittest.TestCase):
    def test_day2A(self):
        self.assertEqual(cube_conundrum_a("test_data.txt"), 8)

    def test_day2B(self):
        self.assertEqual(cube_conundrum_b("test_data.txt"), 2286)



if __name__ == "__main__":
    unittest.main()
