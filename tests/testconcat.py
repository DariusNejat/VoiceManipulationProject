import unittest
import numpy as np
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from libraries.library6 import concatenate_segments

class TestConcatenateSegments(unittest.TestCase):
    def test_concatenate_segments(self):
        segment1 = np.array([1, 2, 3])
        segment2 = np.array([4, 5, 6])
        segment3 = np.array([7, 8, 9])
        segments = [segment1, segment2, segment3]

        concatenated = concatenate_segments(segments)
        expected = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

        np.testing.assert_array_equal(concatenated, expected)

if __name__ == "__main__":
    unittest.main()