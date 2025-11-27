import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    
    def test_area_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        
    def test_area_regular(self):
        res = area(6, 4)
        self.assertEqual(res, 12)
        
    def test_area_float(self):
        res = area(5.5, 2)
        self.assertEqual(res, 5.5)
    
    def test_perimeter_regular(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
        
    def test_perimeter_zero(self):
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 9)
        
    def test_perimeter_negative(self):
        res = perimeter(-1, 4, 5)
        self.assertEqual(res, 8) 

if __name__ == "__main__":
    unittest.main()