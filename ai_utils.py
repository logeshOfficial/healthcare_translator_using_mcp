import requests

API_URL = "https://healthcare-translator-using-mcp.onrender.com/translate" #For deployed MCP server
# API_URL = "http://localhost:8000/translate" #For local testing

def translate_medical_text(text, target_language):
    response = requests.post(
        API_URL,
        json={
            "text": text,
            "target_language": target_language
        },
        timeout=60
    )
    # if response.status_code != 200:
    #     raise ValueError(response.text)
    data = response.json()
    print("API RESPONSE:", data)

    return data.get("text", "❌ Translation failed")
