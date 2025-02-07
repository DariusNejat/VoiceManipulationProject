import numpy as np
import unittest

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

def segment_audio_by_duration(audio_input, sample_rate, segment_duration_ms):
    """
    Segment an audio array into segments of fixed duration.
    
    Parameters:
      - audio_input: A NumPy array representing an audio signal, or a list of such arrays.
      - sample_rate: Sampling rate of the audio.
      - segment_duration_ms: Duration of each segment in milliseconds.
    
    Returns:
      - If a single array is provided, returns a list of segmented NumPy arrays.
      - If a list of arrays is provided, returns a list of lists of segmented arrays.
    """
    # Calculate the segment length in samples.
    segment_length = int(sample_rate * segment_duration_ms / 1000)
    if segment_length <= 0:
        raise ValueError("segment_duration_ms is too short for the given sample_rate")
    
    # If a single audio array is provided, wrap it in a list.
    if isinstance(audio_input, np.ndarray):
        audio_arrays = [audio_input]
    else:
        audio_arrays = audio_input
    
    segmented_audios = []
    for audio in audio_arrays:
        # Slice the audio into segments of 'segment_length' samples.
        segments = [audio[i:i+segment_length] for i in range(0, len(audio), segment_length)]
        segmented_audios.append(segments)
    
    if len(segmented_audios) == 1:
        return segmented_audios[0]
    return segmented_audios

# ---------------------- Unit Tests ---------------------- #
class TestSegmentAudioList(unittest.TestCase):
    def test_segment_audio_list(self):
        sample_rate = 1000  # 1000 samples per second
        num_segments = 2   # Split each audio into 2 segments
        audio1 = np.arange(1000)   # Test signal with values from 0 to 999
        audio2 = np.arange(1500)   # Test signal with values from 0 to 1499
        
        audio_arrays = [audio1, audio2]
        segmented_audios = segment_audio_list(audio_arrays, sample_rate, num_segments)

        # Expected segment lengths.
        expected_segment_samples1 = len(audio1) // num_segments
        expected_segment_samples2 = len(audio2) // num_segments
        
        self.assertEqual(len(segmented_audios[0][0]), expected_segment_samples1)
        self.assertEqual(len(segmented_audios[1][0]), expected_segment_samples2)
        
        # Check if segmentation preserves original values.
        self.assertTrue(np.array_equal(segmented_audios[0][0], np.arange(500)))
        self.assertTrue(np.array_equal(segmented_audios[0][1], np.arange(500, 1000)))
        self.assertEqual(segmented_audios[1][1][-1], 1499)

class TestSegmentAudioByDuration(unittest.TestCase):
    def test_exact_division(self):
        sample_rate = 1000  # 1000 samples per second
        segment_duration_ms = 250  # Each segment is 250ms (i.e., 250 samples)
        audio = np.arange(1000)
        segments = segment_audio_by_duration(audio, sample_rate, segment_duration_ms)
        
        # Expecting exactly 4 segments.
        self.assertEqual(len(segments), 4)
        for segment in segments:
            self.assertEqual(len(segment), 250)
        
        # Verify that reassembling the segments recovers the original audio.
        self.assertTrue(np.array_equal(np.concatenate(segments), audio))

    def test_inexact_division(self):
        sample_rate = 1000  # 1000 samples per second
        segment_duration_ms = 300  # Each segment is 300ms (i.e., 300 samples)
        audio = np.arange(1000)
        segments = segment_audio_by_duration(audio, sample_rate, segment_duration_ms)
        # Expected segmentation:
        # Segment 1: samples 0-299 (300 samples)
        # Segment 2: samples 300-599 (300 samples)
        # Segment 3: samples 600-899 (300 samples)
        # Segment 4: samples 900-999 (100 samples)
        self.assertEqual(len(segments), 4)
        self.assertEqual(len(segments[0]), 300)
        self.assertEqual(len(segments[1]), 300)
        self.assertEqual(len(segments[2]), 300)
        self.assertEqual(len(segments[3]), 100)
        self.assertTrue(np.array_equal(np.concatenate(segments), audio))

if __name__ == "__main__":
    unittest.main()
