import os
import soundfile as sf

def save_audio(audio, sr, output_folder, output_name="output", output_format="wav", bitrate="192k"):
    """Saves the processed audio in different formats with optional settings."""
    try:
        # Ensure output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Define output file path with the desired format
        output_file = os.path.join(output_folder, f"{output_name}.{output_format}")

        # Save the audio with proper format and settings
        if output_format.lower() == "mp3":
            sf.write(output_file, audio, sr, format="MP3", subtype="PCM_16", bitrate=bitrate)
        else:
            sf.write(output_file, audio, sr, format=output_format.upper())

        print(f"Audio saved: {output_file}")
    except Exception as e:
        print(f"Error saving audio: {e}")
