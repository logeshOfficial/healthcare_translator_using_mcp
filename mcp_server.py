from mcp.server.fastmcp import FastMCP
import os
from google import genai
from dotenv import load_dotenv
import config

load_dotenv()

mcp = FastMCP("Healthcare Translator MCP")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

language_map = config.language_map.keys()

@mcp.tool()
def _translate_medical_text(text: str, target_language: str) -> str:
    """
    Corrects speech errors and translates medical text.
    """
    prompt = f"""
You are a professional medical interpreter.
Correct minor speech recognition errors.
Preserve medical meaning.
Translate into {language_map[target_language]}.
Keep language simple and patient-friendly.

Transcript:
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text.strip()

def translate_medical_text(text: str, target_language: str) -> str:
    return _translate_medical_text(text, target_language)


# import os
# from mcp.server.fastmcp import FastMCP
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()

# # Initialize MCP server
# mcp = FastMCP("Healthcare Translator MCP")

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

# language_map = {
#     "English": "English",
#     "Tamil": "Tamil (India)",
#     "Hindi": "Hindi (India)"
# }

# @mcp.tool()
# def translate_medical_text(text: str, target_language: str) -> str:
#     """
#     Translate medical speech into a target language.
#     Fixes minor speech recognition errors and preserves medical meaning.
#     """

#     prompt = f"""
# You are a professional medical interpreter.

# Tasks:
# 1. Correct minor speech recognition errors.
# 2. Preserve medical meaning.
# 3. Translate into {language_map[target_language]}.
# 4. Keep language simple and patient-friendly.

# Transcript:
# {text}
# """

#     try:
#         response = client.models.generate_content(
#             model="gemini-2.5-flash-lite",
#             contents=prompt,
#         )
#         return response.text.strip()
#     except Exception as ex:
#         return f"Translation failed: {ex}"

# if __name__ == "__main__":
#     mcp.run()
