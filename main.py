import os
import librosa
import soundfile as sf

# Import all functions from the libraries package
from libraries import *

# Define paths
DATA_FOLDER = "data"
OUTPUT_FOLDER = "output"

def main():
    print("Welcome to the Voice Manipulation Project!")

    # Load a sample audio file
    input_file = os.path.join(DATA_FOLDER, "sample1.wav")
    if not os.path.exists(input_file):
        print(f"Input file {input_file} not found!")
        return

    # Load the audio and sampling rate
    print("Loading audio file...")
    audio, sr = librosa.load(input_file, sr=None)

    # Apply the processing pipeline
    print("Applying manipulations...")
    audio = segment_voice(audio, sr)  # Function from library1
    audio = reverse_segment(audio, sr)  # Function from library2
    audio = change_pitch(audio, sr, pitch_shift=2)  # Function from library3
    audio = adjust_speed(audio, sr, speed_factor=1.5)  # Function from library4

    # Save the output audio
    output_file = os.path.join(OUTPUT_FOLDER, "manipulated_sample1.wav")
    sf.write(output_file, audio, sr)
    print(f"Manipulated audio saved to {output_file}")

if __name__ == "__main__":
    main()
