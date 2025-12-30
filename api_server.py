from fastapi import FastAPI, HTTPException
from mcp_server import translate_medical_text

app = FastAPI(title="Healthcare Translator API")

@app.post("/translate")
def translate(payload: dict):
    try:
        text = payload["text"]
        target_language = payload["target_language"]

        result = translate_medical_text(text, target_language)

        return {"text": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))