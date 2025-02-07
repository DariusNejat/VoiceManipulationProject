import os
import librosa
import soundfile as sf
# Import all functions from the libraries package
from libraries import *


# Define pathsm
DATA_FOLDER = "data"
OUTPUT_FOLDER = "output"

def main():
    print("Welcome to the Voice Manipulation Project!")
    # Receives and checks Input Duration
    while True:
        try:
            segment_duration_ms = int(input("Please Enter each segment's duration in ms: "))
            if segment_duration_ms <= 0:
                print("Duration can't be less than 1 \n")
                continue
            break
        except ValueError:
            print("The input format is not vaild. try again \n")
            continue
        
    # Receives and checks the File
    while True:
        try:
            file_name = input("Enter the file's name including its extension (It should be present in the data folder): ")
            input_file = os.path.join(DATA_FOLDER, f"{file_name}")
            if not os.path.exists(input_file):
                print(f"Input file {input_file} not found!")
                continue
            break
        except Exception as e:
            print(e)
            continue
        
    # Receives and checks the method
    while True:
        try:
            method = input("What's your manipulation method? type the number of your method:\n 1. Mute\n 2. Whitenoise\n 3. Pinknoise\n 4. Reverse\n Your choice: " )
            if method not in ["1","2","3","4"]:
                print("Invalid input \n")
                continue
            break
        except Exception as e:
            print(e)
            continue

    # Load the audio and sampling rate
    print("Loading audio file...")
    audio, sr = librosa.load(input_file, sr=None)

    # Apply the processing pipeline
    print("Applying manipulations...")
    
    audiolist = segment_audio_by_duration(audio, sr, segment_duration_ms) #Function from library1
    match method:
        case "1":
            audiolist = manipulate_segments(audiolist, "mute", sr, 'white', 0.5) # Function from library3
        case "2":
            audiolist = manipulate_segments(audiolist, "noise", sr, 'white', 0.5) # Function from library3
        case "3":
            audiolist = manipulate_segments(audiolist, "noise", sr, 'pink', 0.5) # Function from library3
        case "4":
            audiolist = reverse_segments(audiolist,'1 * n + 0')  # Function from library2
        case _:
            print("invalid manipulation input.")
    
    audiolist = smooth_audio_list(audiolist, sr, fade_percentage=15)  # Function from library5 audio_arrays, sample_rate, fade_percentage=15
    audio = concatenate_segments(audiolist)  # Function from library6


    # Save in different formats
    # Save the output audio in WAV and MP3 formats.
    while True:
        try:
            output_name = input("Enter the Output's name without it's extension: ")
            break
        except Exception as e:
            print(e)
            continue 
    save_audio(audio, sr, OUTPUT_FOLDER, output_name=output_name, output_format="wav")

if __name__ == "__main__":
    main()
