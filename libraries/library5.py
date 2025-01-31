import numpy as np

def smooth_audio_list(audio_arrays, sample_rate, fade_percentage=15):
    """
    Apply fade-in and fade-out smoothing to a list of audio arrays.

    Parameters:
    - audio_arrays: List of NumPy arrays representing audio signals.
    - sample_rate: Sampling rate of the audio.
    - fade_percentage: Percentage of the audio duration to apply fade in/out (default: 15%).

    Returns:
    - List of smoothed audio arrays.
    """
    if not (0 <= fade_percentage <= 50): # checks to see if the fade_percentage is withing desired bounds.
        raise ValueError("The fade_percentage must be between 0 and 50.")

    fade_percentage /= 100  # Convert to fraction
    smoothed_audios = []

    for audio in audio_arrays:
        fade_samples = int(len(audio) * fade_percentage)
        fade_in = np.linspace(0.0, 1.0, fade_samples) #used for fade-in
        fade_out = np.linspace(1.0, 0.0, fade_samples) #used for fade-out

        audio[:fade_samples] *= fade_in #applies fade-in
        audio[-fade_samples:] *= fade_out #applies fade-out

        smoothed_audios.append(audio)

    return smoothed_audios


import unittest
import numpy as np
from .smoothing import smooth_audio_list

#This is a test for the smooth_audio_list function.

class TestSmoothAudioList(unittest.TestCase):
    def test_smooth_audio_list(self):
        sample_rate = 44100
        fade_percentage = 40
        fade_percentage_divided = fade_percentage / 100

        audio1 = np.ones(2000)
        audio2 = np.linspace(2, 10, 1000)

        audio_arrays = [audio1, audio2]
        smoothed_audios = smooth_audio_list(audio_arrays, sample_rate, fade_percentage) #We created a sample list of audio arrays.

        self.assertEqual(len(audio1), len(smoothed_audios[0])) #checks to see the length of the first audio hasn't changed.
        self.assertEqual(len(audio2), len(smoothed_audios[1])) #checks to see the length of the second audio hasn't changed.

        fade_samples1 = int(len(audio1) * fade_percentage_divided)
        fade_samples2 = int(len(audio2) * fade_percentage_divided)

        self.assertTrue(np.all(smoothed_audios[0][:fade_samples1] > 0)) # for the first audio, Checks fade-in.
        self.assertTrue(np.all(smoothed_audios[0][-fade_samples1:] < 1))

        self.assertTrue(np.all(smoothed_audios[1][:fade_samples2] > 0)) # for the second audio, Checks fad-in.
        self.assertTrue(np.all(smoothed_audios[1][-fade_samples2:] < 1))

if __name__ == "__main__":
    unittest.main()
