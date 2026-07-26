from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from core.transcriber import transcribe_all
from utilities.audio_processor import process_input
import os

print("Model:", repr(os.getenv("SARVAM_STT_MODEL")))
print("KEY LOADED:", os.getenv("SARVAM_API_KEY")) #should print the key value from .env file
print("CWS:", os.getcwd())

source = "https://www.youtube.com/watch?v=WFnGg9w_Hdo"
language = "hinglish"  #change to "hinglish" to start Sarvam

chunks = process_input(source)
transcript = transcribe_all(chunks, language=language)

print("\n== TRANSCRIPT ==\n")
print(transcript)