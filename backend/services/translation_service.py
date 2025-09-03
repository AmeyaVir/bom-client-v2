import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class TranslationService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def translate_to_english(self, text: str) -> str:
        """Translates Japanese text to English using Gemini API."""
        prompt = f"""
        Translate the following text from Japanese to English. Maintain all original formatting, including line breaks and tables.
        
        Japanese Text:
        {text}
        
        English Translation:
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error calling Gemini API for translation: {e}")
            return text
      
