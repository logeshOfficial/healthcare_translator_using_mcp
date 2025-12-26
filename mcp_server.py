import os
from mcp.server.fastmcp import FastMCP
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize MCP server
mcp = FastMCP("Healthcare Translator MCP")

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

language_map = {
    "English": "English",
    "Tamil": "Tamil (India)",
    "Hindi": "Hindi (India)"
}

@mcp.tool()
def translate_medical_text(text: str, target_language: str) -> str:
    """
    Translate medical speech into a target language.
    Fixes minor speech recognition errors and preserves medical meaning.
    """

    prompt = f"""
You are a professional medical interpreter.

Tasks:
1. Correct minor speech recognition errors.
2. Preserve medical meaning.
3. Translate into {language_map[target_language]}.
4. Keep language simple and patient-friendly.

Transcript:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
        )
        return response.text.strip()
    except Exception as ex:
        return f"Translation failed: {ex}"

if __name__ == "__main__":
    mcp.run()
