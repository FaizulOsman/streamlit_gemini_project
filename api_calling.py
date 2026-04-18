from google import genai
from dotenv import load_dotenv
import os
import io
from gtts import gTTS
import streamlit as st

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Note Generator
def note_generator(images):
    prompt = """Summarize these pictures in note format at max 100 words, 
    make sure to add necessary markdown to differentiate different section."""
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text

def audio_transcription(text):
    speech = gTTS(text, lang="en", slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(images, difficulty):
    prompt = f"""Generate 3 quizzes based on the {difficulty}. 
    Make sure to add markdown to differenciate the options."""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text