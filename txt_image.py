from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from huggingface_hub import InferenceClient
import io
import os
from fastapi.responses import StreamingResponse
load_dotenv()
app = FastAPI()
HF_TOKEN = os.getenv("HF_TOKEN")

class PromptIn(BaseModel):
    prompt: str


client = InferenceClient(token=HF_TOKEN)

@app.post("/predict")
def predict_premium(data: PromptIn):
    """
    Accepts JSON: { "prompt": "..." }
    Returns: PNG image bytes (image/png)
    """
    # Format prompt with the PromptTemplate (returns plain string)
    prompt_text = data.prompt

    try:
        # Generate image (this returns a PIL.Image.Image in huggingface_hub InferenceClient)
        image = client.text_to_image(
            prompt=prompt_text,
            model="black-forest-labs/FLUX.1-schnell",
        )

        # Convert to bytes
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")

    except Exception as e:
        # Return helpful error for debugging
        raise HTTPException(status_code=500, detail=str(e))

