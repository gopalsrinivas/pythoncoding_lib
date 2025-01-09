import os
import speech_recognition as sr
from pydub import AudioSegment
from datetime import datetime


def convert_audio_to_text(audio_file_path):
    """
    Converts an audio file (MP3 or WAV) to text using Google's Speech Recognition API.
    """
    try:
        # Check if the file exists
        if not os.path.exists(audio_file_path):
            print("Error: File not found.")
            return "Error: File not found."

        # Check the file format and convert to WAV if necessary
        if audio_file_path.endswith(".mp3"):
            print("MP3 file detected. Converting to WAV format...")
            audio = AudioSegment.from_mp3(audio_file_path)
            audio_file_path = os.path.splitext(audio_file_path)[0] + ".wav"
            audio.export(audio_file_path, format="wav")
            print(f"MP3 converted to WAV: {audio_file_path}")

        # Initialize recognizer
        recognizer = sr.Recognizer()

        # Process the audio file
        with sr.AudioFile(audio_file_path) as source:
            print(f"Loading WAV file: {audio_file_path}...")
            audio_data = recognizer.record(source)
            print("Audio data extracted successfully.")

        # Recognize speech
        print("Recognizing text from audio...")
        try:
            text = recognizer.recognize_google(audio_data)
            print("Text recognition successful.")
            return text
        except sr.UnknownValueError:
            print("Error: Could not understand the audio.")
            return "Error: Could not understand the audio."
        except sr.RequestError as e:
            print(f"Error: Could not request results from the API; {e}")
            return f"Error: Could not request results from the API; {e}"

    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Unexpected error: {e}"


def save_text_without_timestamp(text, output_file_path):
    """
    Saves text without the timestamp to a .txt file.
    """
    try:
        print(f"Saving text to {output_file_path}...")
        # Save only the extracted text without the timestamp
        with open(output_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text + "\n")
        print(f"Text successfully saved to {output_file_path}")
    except Exception as e:
        print(f"Error while saving to .txt file: {e}")


if __name__ == "__main__":
    # Base directory and file name
    base_dir = r"D:\\professional\\pythoncoding_lib"
    audio_file_name = "female-voice-audio_to_text.wav"

    # Generate timestamp for the output file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{timestamp}_output_audio_to_text.txt"

    # Generate full dynamic paths
    audio_file_path = os.path.join(base_dir, audio_file_name)
    text_file_path = os.path.join(base_dir, output_filename)

    # Convert audio to text
    print(f"Starting transcription process for {audio_file_path}...")
    transcribed_text = convert_audio_to_text(audio_file_path)

    # If transcription is successful, save it to a .txt file without timestamp
    if "Error" not in transcribed_text:
        save_text_without_timestamp(transcribed_text, text_file_path)
    else:
        print("Transcription failed:", transcribed_text)

    print("Process completed.")
