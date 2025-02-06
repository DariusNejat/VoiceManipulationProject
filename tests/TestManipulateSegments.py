import numpy as np
import unittest
from libraries.library3 import *

class TestManipulateSegments(unittest.TestCase):
    def setUp(self):
        #create sample audio segments
        self.segment1 = np.ones(1000)      #array of ones
        self.segment2 = np.full(1000, 2)   #array of twos
        self.segment3 = np.full(1000, 3)   #array of threes
        self.segment4 = np.full(1000, 4)   #array of fours
        self.audio_segments = [self.segment1, self.segment2, self.segment3, self.segment4]
        self.sample_rate = 44100  
    def test_mute_method(self):
        #test the 'mute' method
        manipulated_segments = manipulate_segments(
            self.audio_segments, method='mute', sample_rate=self.sample_rate
        )

        #check that segments with even indices are muted
        self.assertTrue(np.all(manipulated_segments[0] == 0))  # Index 0 should be muted
        self.assertTrue(np.all(manipulated_segments[2] == 0))  # Index 2 should be muted

        #check that the other segments are unchanged
        self.assertTrue(np.array_equal(manipulated_segments[1], self.segment2))
        self.assertTrue(np.array_equal(manipulated_segments[3], self.segment4))

        #check that the length of the output matches the input
        self.assertEqual(len(manipulated_segments), len(self.audio_segments))

    def test_noise_method_white(self):
        #test the 'noise' method with white noise
        manipulated_segments = manipulate_segments(
            self.audio_segments, method='noise', sample_rate=self.sample_rate,
            noise_type='white', noise_level=0.5
        )

        #check that segments with even indices have noise added
        self.assertFalse(np.array_equal(manipulated_segments[0], self.segment1))
        self.assertFalse(np.array_equal(manipulated_segments[2], self.segment3))

        #check that the other segments are unchanged
        self.assertTrue(np.array_equal(manipulated_segments[1], self.segment2))
        self.assertTrue(np.array_equal(manipulated_segments[3], self.segment4))

        #verify that the noise is correctly scaled using RMS
        original_rms = calculate_rms(self.segment1)
        noise_rms = calculate_rms(manipulated_segments[0])

        expected_rms = original_rms * 0.5  # noise_level * original RMS
        self.assertAlmostEqual(noise_rms, expected_rms, delta=0.1 * expected_rms)

    def test_noise_method_pink(self):
        #test the 'noise' method with pink noise
        manipulated_segments = manipulate_segments(
            self.audio_segments, method='noise', sample_rate=self.sample_rate,
            noise_type='pink', noise_level=0.5
        )

        #check that segments with even indices have noise added
        self.assertFalse(np.array_equal(manipulated_segments[0], self.segment1))
        self.assertFalse(np.array_equal(manipulated_segments[2], self.segment3))

        #check that the other segments are unchanged
        self.assertTrue(np.array_equal(manipulated_segments[1], self.segment2))
        self.assertTrue(np.array_equal(manipulated_segments[3], self.segment4))

        #check that the length of the output matches the input
        self.assertEqual(len(manipulated_segments), len(self.audio_segments))

    def test_noise_scaling_with_rms(self):
        #test noise scaling using RMS values
        manipulated_segments = manipulate_segments(
            self.audio_segments, method='noise', sample_rate=self.sample_rate,
            noise_type='white', noise_level=0.7
        )

        #calculate RMS values
        original_rms = calculate_rms(self.segment1)
        noise_rms = calculate_rms(manipulated_segments[0])

        expected_rms = original_rms * 0.7  # noise_level * original RMS
        self.assertAlmostEqual(noise_rms, expected_rms, delta=0.1 * expected_rms)

    def test_invalid_method(self):
        #test with an invalid method
        with self.assertRaises(ValueError):
            manipulate_segments(self.audio_segments, method='invalid', sample_rate=self.sample_rate)

    def test_invalid_sample_rate_type(self):
        #test with invalid sample rate type
        with self.assertRaises(TypeError):
            manipulate_segments(self.audio_segments, method='mute', sample_rate='44100')

    def test_invalid_sample_rate_value(self):
        #test with invalid sample rate value (negative number)
        with self.assertRaises(ValueError):  # Updated to expect ValueError
            manipulate_segments(self.audio_segments, method='mute', sample_rate=-44100)

    def test_invalid_noise_type(self):
        #test with an unsupported noise type
        with self.assertRaises(ValueError):
            manipulate_segments(self.audio_segments, method='noise', sample_rate=self.sample_rate, noise_type='blue')

    def test_invalid_inputs(self):
        #test with invalid inputs
        with self.assertRaises(TypeError):
            manipulate_segments("not a list", method='mute', sample_rate=self.sample_rate)
        with self.assertRaises(TypeError):
            manipulate_segments([1, 2, 3], method='mute', sample_rate=self.sample_rate)
        with self.assertRaises(TypeError):
            manipulate_segments([np.ones(1000), "not an array"], method='mute', sample_rate=self.sample_rate)

if __name__ == '__main__':
    unittest.main()
