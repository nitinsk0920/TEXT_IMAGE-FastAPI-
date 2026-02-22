
from fastapi import FastAPI, HTTPException
import io
from fastapi.responses import StreamingResponse
from schema.userinput import PromptIn
from model.model import predict_output,MODEL_VERSION 

app = FastAPI()
@app.get('/')
def home():
    return {'message':'TEXT-TO-IMAGE CONVERSION API'}

# machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
    }

@app.post("/predict")
def predict_premium(data: PromptIn):

    prompt_text = data.prompt

    try:
        # Generate image (this returns a PIL.Image.Image in huggingface_hub InferenceClient)
        image = predict_output(prompt_text)
        # Convert to bytes
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")

    except Exception as e:
        # Return helpful error for debugging
        raise HTTPException(status_code=500, detail=str(e))

