import os
import librosa
import soundfile as sf

# Import all functions from the libraries package
from libraries import *

# Define paths
DATA_FOLDER = "data"
OUTPUT_FOLDER = "output"
num_segments = 6



def main():
    print("Welcome to the Voice Manipulation Project!")
    method = input("whats ur manipulation method? type mute or whitenoise or pinknoise or reverse" )
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
    audiolist = segment_audio_list(audio, sr, num_segments)  # Function from library1
    match method:
        case "mute":
            audiolist = manipulate_segments(audiolist, "mute", sr, 'white', 0.5) # Function from library3
        case "whitenoise":
            audiolist = manipulate_segments(audiolist, "noise", sr, 'white', 0.5) # Function from library3
        case "pinknoise":
            audiolist = manipulate_segments(audiolist, "noise", sr, 'pink', 0.5) # Function from library3
        case "reverse":
            audiolist = reverse_segments(audiolist,'2 * n + 0')  # Function from library2
        case _:
            print("invalid manipulation input.")
    audiolist = smooth_audio_list(audiolist, sr, pitch_shift=2)  # Function from library5
    audio = concatenate_segments(audiolist)  # Function from library6

    # Save the output audio
    output_file = os.path.join(OUTPUT_FOLDER, "manipulated_sample1.wav")
    sf.write(output_file, audio, sr)
    print(f"Manipulated audio saved to {output_file}")

if __name__ == "__main__":
    main()
