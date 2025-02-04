import numpy as np
import unittest

def segment_audio_list(audio_arrays, sample_rate, segment_length_sec):
    """
    Segment each audio array into smaller segments of a given length.

    Parameters:
    - audio_arrays: List of NumPy arrays representing audio signals.
    - sample_rate: Sampling rate of the audio.
    - segment_length_sec: Desired segment length in seconds.

    Returns:
    - List of lists, where each sublist contains segmented NumPy arrays.
    """
    if segment_length_sec <= 0:
        raise ValueError("segment_length_sec must be greater than 0.")
    
    segment_samples = int(segment_length_sec * sample_rate)
    
    segmented_audios = []
    for audio in audio_arrays:
        segments = [audio[i:i + segment_samples] for i in range(0, len(audio), segment_samples)]
        segmented_audios.append(segments)
    
    return segmented_audios


class TestSegmentAudioList(unittest.TestCase):
    def test_segment_audio_list(self):
        sample_rate = 1000  # 1000 samples per second
        segment_length_sec = 0.5  # 0.5 seconds per segment
        audio1 = np.arange(1000)  # A simple test signal with values from 0 to 999
        audio2 = np.arange(1500)  # A second test signal with values from 0 to 1499
        
        audio_arrays = [audio1, audio2]
        segmented_audios = segment_audio_list(audio_arrays, sample_rate, segment_length_sec)

        # Check if each segment is of expected length
        expected_segment_samples = int(segment_length_sec * sample_rate)
        self.assertEqual(len(segmented_audios[0][0]), expected_segment_samples)  # First segment of audio1
        self.assertEqual(len(segmented_audios[1][0]), expected_segment_samples)  # First segment of audio2
        
        # Check if the number of segments is correct
        self.assertEqual(len(segmented_audios[0]), 2)  # 1000 samples, split into 2 segments
        self.assertEqual(len(segmented_audios[1]), 3)  # 1500 samples, split into 3 segments
        
        # Check if segmentation preserves original values
        self.assertTrue(np.array_equal(segmented_audios[0][0], np.arange(500)))
        self.assertTrue(np.array_equal(segmented_audios[0][1], np.arange(500, 1000)))
        self.assertTrue(np.array_equal(segmented_audios[1][2], np.arange(1000, 1500)))

if __name__ == "__main__":
    unittest.main()
