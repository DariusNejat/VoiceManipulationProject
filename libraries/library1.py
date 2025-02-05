import numpy as np
import unittest

def segment_audio_list(audio_arrays, sample_rate, num_segments):
    """
    Segment each audio array into a given number of segments.

    Parameters:
    - audio_arrays: List of NumPy arrays representing audio signals.
    - sample_rate: Sampling rate of the audio.
    - num_segments: Number of segments to split each audio into.

    Returns:
    - List of lists, where each sublist contains segmented NumPy arrays.
    """
    if num_segments <= 0:
        raise ValueError("num_segments must be greater than 0.")
    
    segmented_audios = []
    for audio in audio_arrays:
        segment_samples = len(audio) // num_segments
        segments = [audio[i * segment_samples:(i + 1) * segment_samples] for i in range(num_segments)]
        
        # Handle remainder samples if the split isn't exact
        if len(audio) % num_segments != 0:
            segments[-1] = np.concatenate((segments[-1], audio[num_segments * segment_samples:]))
        
        segmented_audios.append(segments)
    
    return segmented_audios


class TestSegmentAudioList(unittest.TestCase):
    def test_segment_audio_list(self):
        sample_rate = 1000  # 1000 samples per second
        num_segments = 2  # Split each audio into 2 segments
        audio1 = np.arange(1000)  # A simple test signal with values from 0 to 999
        audio2 = np.arange(1500)  # A second test signal with values from 0 to 1499
        
        audio_arrays = [audio1, audio2]
        segmented_audios = segment_audio_list(audio_arrays, sample_rate, num_segments)

        # Check if each segment is of expected length
        expected_segment_samples1 = len(audio1) // num_segments
        expected_segment_samples2 = len(audio2) // num_segments
        
        self.assertEqual(len(segmented_audios[0][0]), expected_segment_samples1)
        self.assertEqual(len(segmented_audios[1][0]), expected_segment_samples2)
        
        # Check if segmentation preserves original values
        self.assertTrue(np.array_equal(segmented_audios[0][0], np.arange(500)))
        self.assertTrue(np.array_equal(segmented_audios[0][1], np.arange(500, 1000)))
        self.assertTrue(np.array_equal(segmented_audios[1][1][-1], 1499))

if __name__ == "__main__":
    unittest.main()
