import re
import unittest
import numpy as np



def pattern_decoder(pattern:str):
    """
    Return the multiplier and the constant in the pattern
     
    Paramaters:
        pattern (str): should follow this pattern: MULT * var * CONS, where var can be any letter and MULT & CONS can be float or int.
        MULT and CONS are required. use 1 * n + 0 if you mean a pattern which only includes n.
    Raises:
        Exception: if the pattern does not match the format, an exception will be raised.

    Returns:
        Multiplier (float): the multiplier in the pattern
        Constant (float): The constant in the pattern
    """
    pattern = pattern.replace(' ','')
    if re.match(r'(\d|\d\.\d)(\*)([a-zA-Z])((\+|\-)(\d|(\d.\d)))', pattern):
        multiplier = float(re.findall(r'(\d|\d\.\d)(\*)([a-zA-Z])((\+|\-)(\d|(\d\.\d)))',pattern)[0][0])
        constant = float(re.findall(r'(\d|\d\.\d)(\*)([a-zA-Z])((\+|\-)(\d\.\d|\d))',pattern)[0][3])
    else:
        raise Exception(f"The pattern: '{pattern}' does not match the following pattern: 'multiplier * n + constant'")
    
    return multiplier,constant


def reverse_segments(segments_list: list,sr,pattern: str = '2 * n + 0'):
    
    """
    Reverses the segments whose index follows the pattern.
    
    Parameters:
        segments_list (list): list of the segments/audios. if only one audio is to be reversed, pass it in a list
        pattern (str): the pattern which is used to select the segments. Should follow this pattern: 'MULT * var * CONS', where 'var' can be any letter and 'MULT' & 'CONS' can be float or int. 'MULT and CONS' are required. 
        Use 1 * n + 0 if you mean a pattern which includes all the segments.

    Returns:
        segments_list (list): the list of segments.
    """
    try:
        multiplier, constant = pattern_decoder(pattern)
        i = 0
        while multiplier * i + constant < len(segments_list):
            segments_list[i] = segments_list[i][::-1]
            i += 1
        return segments_list
    except Exception as e:
        raise e
        
        
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