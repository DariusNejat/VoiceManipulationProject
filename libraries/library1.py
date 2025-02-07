import numpy as np
import unittest

import numpy as np

def segment_audio_list(audio_input, sample_rate, num_segments):
    """
    Segment an audio array into a given number of segments.
    
    Parameters:
      - audio_input: A NumPy array representing an audio signal, or a list of such arrays.
      - sample_rate: Sampling rate of the audio (provided for consistency, though not used here).
      - num_segments: Number of segments to split the audio into.
    
    Returns:
      - If a single array is provided, returns a list of segmented NumPy arrays.
      - If a list of arrays is provided, returns a list of lists of segmented arrays.
    """
    if num_segments <= 0:
        raise ValueError("num_segments must be greater than 0.")
    
    # If a single audio array is provided, wrap it in a list.
    if isinstance(audio_input, np.ndarray):
        audio_arrays = [audio_input]
    else:
        audio_arrays = audio_input

    segmented_audios = []
    for audio in audio_arrays:
        segment_samples = len(audio) // num_segments
        segments = [audio[i * segment_samples:(i + 1) * segment_samples] for i in range(num_segments)]
        
        # Append any remaining samples to the last segment if needed.
        remainder = len(audio) % num_segments
        if remainder:
            segments[-1] = np.concatenate((segments[-1], audio[num_segments * segment_samples:]))
        
        segmented_audios.append(segments)
    
    # If the input was a single array, return its segments directly.
    if len(segmented_audios) == 1:
        return segmented_audios[0]
    
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
