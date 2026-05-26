# Enterprise-AI-Meeting-Assistant/src/llm_helper.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(prompt):

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Error generating response: {str(e)}"