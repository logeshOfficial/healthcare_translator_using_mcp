from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Healthcare Translator API")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

language_map = {
    "English": "English",
    "Tamil": "Tamil (India)",
    "Hindi": "Hindi (India)"
}

# -------- Request Schema --------
class TranslateRequest(BaseModel):
    text: str
    target_language: str

# -------- Core Translation Logic (shared) --------
def translate_medical_text_core(text: str, target_language: str) -> str:
    if target_language not in language_map:
        raise ValueError("Unsupported language")

    prompt = f"""
You are a professional medical interpreter.
Correct minor speech recognition errors.
Preserve medical meaning.
Translate to {language_map[target_language]}.
Keep it simple and patient-friendly.

STRICT OUTPUT RULES:
- Output ONLY the translated sentence.
- Do NOT include explanations.
- Do NOT include headings.
- Do NOT include markdown symbols like ** or bullet points.
- Do NOT add phonetics or extra lines.

Transcript:
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text.strip()

# -------- REST Endpoint --------
@app.post("/translate")
def translate(req: TranslateRequest):
    try:
        result = translate_medical_text_core(
            req.text,
            req.target_language
        )
        return {"translated_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))