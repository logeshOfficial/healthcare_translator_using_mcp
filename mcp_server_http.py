from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
import os
from google import genai
from dotenv import load_dotenv
import config

load_dotenv()

app = FastAPI()
mcp = FastMCP("Healthcare Translator MCP")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

language_map = config.language_map

@mcp.tool()
def translate_medical_text(text: str, target_language: str) -> str:
    prompt = f"""
You are a professional medical interpreter.
Correct speech errors, preserve meaning.
Translate to {language_map[target_language]}.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"{prompt}\n{text}"
    )
    return response.text.strip()


# Expose ASGI app for uvicorn
app = mcp.sse_app