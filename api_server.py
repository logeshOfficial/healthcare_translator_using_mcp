from fastapi import FastAPI, HTTPException
from mcp_server import translate_medical_text
from pydantic import BaseModel

app = FastAPI(title="Healthcare Translator API")

class TranslateRequest(BaseModel):
    text: str
    target_language: str
    
# Health check endpoint (required by Render)
@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/translate")
def translate(req: TranslateRequest):
    try:
        result = translate_medical_text(req.text, req.target_language)

        return {"text": result["text"]}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))