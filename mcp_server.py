from mcp.server.fastmcp import FastMCP
import os
from google import genai
from dotenv import load_dotenv
import config

load_dotenv()

mcp = FastMCP("Healthcare Translator MCP")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

language_map = config.language_map

@mcp.tool()
def _translate_medical_text(text: str, target_language: str) -> str:
    """
    Corrects speech errors and translates medical text.
    """
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

    if not response.text:
        raise ValueError("Empty response from Gemini")

    return {"text": response.text}

def translate_medical_text(text: str, target_language: str) -> str:
    return _translate_medical_text(text, target_language)
