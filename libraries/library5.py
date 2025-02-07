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
