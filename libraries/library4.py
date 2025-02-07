import os
import numpy as np
import soundfile as sf

def save_audio(audio, sr, output_folder, output_name="output", output_format="wav", bitrate="192k"):
    """Saves the processed audio in different formats with optional settings."""
    try:
        # Ensure output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Define output file path with the desired format
        output_file = os.path.join(output_folder, f"{output_name}.{output_format}")

        if output_format.lower() == "mp3":
            # Use Pydub to export as MP3 with bitrate.
            from pydub import AudioSegment

            # Convert float audio (range [-1, 1]) to int16 (range [-32768, 32767])
            audio_int16 = np.int16(audio * 32767)

            # Create an AudioSegment instance.
            # Adjust channels if needed (here, it's set to 1 for mono).
            audio_segment = AudioSegment(
                audio_int16.tobytes(),
                frame_rate=sr,
                sample_width=audio_int16.dtype.itemsize,
                channels=1
            )

            # Export the audio segment as an MP3 with the specified bitrate.
            audio_segment.export(output_file, format="mp3", bitrate=bitrate)
        else:
            # For non-MP3 formats (like WAV), use soundfile.
            sf.write(output_file, audio, sr, format=output_format.upper())

        print(f"Audio saved: {output_file}")
    except Exception as e:
        print(f"Error saving audio: {e}")
