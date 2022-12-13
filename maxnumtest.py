import unittest
import maxnum as theMax
class testMax(unittest.TestCase): # test class
    def test_max(self):
        self.assertEqual(theMax.theFunction(2, 1), 2)
        self.assertEqual(theMax.theFunction(5, 1), 5)
        self.assertEqual(theMax.theFunction(10, 12), 12)
unittest.main(argv=[''], verbosity=2, exit=False)
