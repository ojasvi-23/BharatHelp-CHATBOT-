# -*- coding: utf-8 -*-
"""Voice Input with Whisper ASR

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IpepmmN9AxUbydEwFTxk71cmzq0nqTdC
"""

# Step 5: Voice Input with Whisper ASR

# Load the Whisper ASR model.
# 'base' is a good balance of size and accuracy for many use cases.
# Other options: 'tiny', 'small', 'medium', 'large'. '_en' suffix for English-only.
# The first time you run this, it will download the model, which can take some time.
print("Loading Whisper ASR model...")
try:
    whisper_model = whisper.load_model("base")
    print("Whisper ASR model loaded successfully.")
except Exception as e:
    print(f"Error loading Whisper model: {e}")
    print("Please ensure you have enough RAM in your Colab instance (Runtime -> Change runtime type -> High-RAM).")
    # Fallback to a smaller model if 'base' fails, or instruct user to try again.
    # whisper_model = whisper.load_model("tiny")
    # print("Loaded 'tiny' Whisper model as fallback.")


# Function to transcribe audio
def transcribe_audio(audio_path):
    """
    Transcribes an audio file using the loaded Whisper model.
    """
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found at {audio_path}")
        return None
    print(f"Transcribing audio from: {audio_path}...")
    try:
        # Whisper can directly process audio files
        result = whisper_model.transcribe(audio_path)
        transcription = result["text"]
        print(f"Transcription: '{transcription}'")
        return transcription
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

# --- Mock Audio Input for Colab ---
# In a real application, you'd capture live microphone input.
# For Colab, we'll simulate by creating a dummy audio file or using a pre-existing one.
# You can upload a .mp3 or .wav file to your Colab environment.

# Create a dummy audio file (requires pydub and ffmpeg/libav-tools)
# Colab usually has ffmpeg pre-installed.
dummy_audio_path_en = "hello_bharathelp.wav"
dummy_audio_path_hi = "namaste_bharathelp.wav"

# You would typically record audio or use pre-recorded files.
# For demonstration, let's assume you have these files or can generate them.
# Example of generating a silent audio file (not useful for transcription, but for structure)
# AudioSegment.silent(duration=2000).export(dummy_audio_path_en, format="wav")
# AudioSegment.silent(duration=2000).export(dummy_audio_path_hi, format="wav")

# To truly test, you'd need actual audio files.
# For example, you could upload a short WAV file saying "Hello BharatHelp" and "नमस्ते भारतहेल्प".
# If you don't have audio files, you can skip this part for now and focus on text input.

# Example usage with a placeholder audio file (you need to upload actual audio files)
print("\n--- Testing Whisper ASR (Requires actual audio files) ---")

# Placeholder: If you upload 'hello_bharathelp.wav' saying "What are the plans for BharatMobile?"
# transcribed_text_en = transcribe_audio(dummy_audio_path_en)
# if transcribed_text_en:
#     print(f"Transcribed English Query: {transcribed_text_en}")
#     # You would then pass this to your qa_chain:
#     # result = qa_chain({"query": transcribed_text_en})
#     # print(f"BharatHelp: {result['result']}")

# Placeholder: If you upload 'namaste_bharathelp.wav' saying "भारतकनेक्ट के प्लान क्या हैं?"
# transcribed_text_hi = transcribe_audio(dummy_audio_path_hi)
# if transcribed_text_hi:
#     print(f"Transcribed Hindi Query: {transcribed_text_hi}")
#     # You would then pass this to your qa_chain:
#     # result = qa_chain({"query": transcribed_text_hi})
#     # print(f"BharatHelp: {result['result']}")

print("\nWhisper ASR setup complete. Remember to provide actual audio files for testing.")
print("For live microphone input, you would need a more complex setup, typically a web frontend.")