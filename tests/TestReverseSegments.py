import unittest
import numpy as np
from libraries import *
class TestReverseSegments(unittest.TestCase):
    
    def setUp(self):
        self.segment1 = np.array([1,2,3])
        self.segment2 = np.array([4,5,6])
        self.segment3 = np.array([7,8,9])
        self.segments = [self.segment1, self.segment2, self.segment3]
        
    def test_reverse_segments1(self):
        reversed_segments = reverse_segments(self.segments, 44100, '1*n+0')
        true_reverses = [np.array([3,2,1]), np.array([6,5,4]), np.array([9,8,7])]
        self.assertEqual(reversed_segments[0].all(),true_reverses[0].all())
        self.assertEqual(reversed_segments[1].all(),true_reverses[1].all())
        self.assertEqual(reversed_segments[2].all(),true_reverses[2].all())
        
        # Test the function with a different pattern.
    def test_reverse_segments2(self):
        reversed_segments = reverse_segments(self.segments, 44100, '2*n+0')
        true_reverses = [np.array([3,2,1]), np.array([4,5,6]), np.array([9,8,7])]
        self.assertEqual(reversed_segments[0].all(),true_reverses[0].all())
        self.assertEqual(reversed_segments[1].all(),true_reverses[1].all())
        self.assertEqual(reversed_segments[2].all(),true_reverses[2].all())
        
        
    
        
if __name__ == "__main__":
    unittest.main()