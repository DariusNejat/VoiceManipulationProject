import numpy as np
import librosa
import scipy.signal


def calculate_rms(signal):
    """
    Calculate the Root Mean Square (RMS) of a signal using librosa.

    Parameters:
    - signal: NumPy array representing the audio signal.

    Returns:
    - RMS value of the signal.
    """
    #librosa.feature.rms returns an array with shape (1, frames)
    rms = librosa.feature.rms(y=signal)
    #compute the mean RMS over all frames
    return np.mean(rms)

def generate_noise(length, sample_rate, noise_type='white'):
    """
    Generate a noise array of a given length and type.

    Parameters:
    - length: Length of the noise array.
    - sample_rate: Sampling rate of the audio (in Hz).
    - noise_type: Type of noise to generate ('white', 'pink').

    Returns:
    - NumPy array containing the generated noise.
    """
    if noise_type == 'white':
        #random samples from a normal distribution
        noise = np.random.normal(0, 1, length)
    elif noise_type == 'pink':
        #generate pink noise by filtering white noise
        white_noise = np.random.normal(0, 1, length)

        #apply a 1/f filter to white noise to approximate pink noise
       
        b = scipy.signal.firwin(
            numtaps=101,
            cutoff=[0.01, 0.5],
            window='hann',  
            pass_zero=False,
            fs=sample_rate
        )
        pink_noise = scipy.signal.lfilter(b, [1.0], white_noise)
        noise = pink_noise
    else:
        raise ValueError("Unsupported noise type. Choose 'white' or 'pink'.")

    #normalize noise to have zero mean and unit variance
    noise = (noise - np.mean(noise)) / (np.std(noise) + 1e-6)
    return noise[:length]  #ensure that the noise array has the correct length

def manipulate_segments(segmented_audios, method, sample_rate, noise_type='white', noise_level=0.5):
    """
    Manipulate audio segments based on the specified method.

    Parameters:
    - segmented_audios: List of NumPy arrays representing audio segments.
    - method: Method to manipulate segments ('mute' or 'noise').
    - sample_rate: Sampling rate of the audio (in Hz). Must be a positive number.
    - noise_type: Type of noise to add ('white', 'pink'); used only if method is 'noise'.
    - noise_level: Amplitude scaling factor for the noise (default: 0.5); used only if method is 'noise'.

    Returns:
    - List of audio segments with specified manipulation applied to segments with even indices.
    """
    #validate input types
    if not isinstance(segmented_audios, list):
        raise TypeError("segmented_audios must be a list of NumPy arrays.")
    if any(not isinstance(seg, np.ndarray) for seg in segmented_audios):
        raise TypeError("Each item in segmented_audios must be a NumPy array.")
    if not isinstance(sample_rate, (int, float)):
        raise TypeError("sample_rate must be an integer or float.")
    if sample_rate <= 0:
        raise ValueError("sample_rate must be a positive number.")  # Added validation
    if method not in ['mute', 'noise']:
        raise ValueError("method must be either 'mute' or 'noise'.")

    manipulated_segments = []

    for i, seg in enumerate(segmented_audios):
        if i % 2 == 0:  #manipulate segments with even indices
            if method == 'mute':
                #mute the segment by replacing it with zeros
                manipulated_seg = np.zeros_like(seg)
            elif method == 'noise':
                #generate noise segment
                noise_seg = generate_noise(len(seg), sample_rate, noise_type=noise_type)

                #calculate RMS values using librosa
                original_rms = calculate_rms(seg)
                noise_rms = calculate_rms(noise_seg) + 1e-6  #prevent division by zero

                #scale noise to match the RMS of the original segment, adjusted by noise_level
                scaled_noise = (noise_seg / noise_rms) * original_rms * noise_level

                manipulated_seg = scaled_noise
            manipulated_segments.append(manipulated_seg)
        else:
            #leave the segment unchanged
            manipulated_segments.append(seg)

    return manipulated_segments