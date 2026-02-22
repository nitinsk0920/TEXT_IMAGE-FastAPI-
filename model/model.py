from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient


load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_VERSION = "stable-diffusion-xl-base-1.0"
client = InferenceClient(token=HF_TOKEN)

def predict_output(data: str):

    prompt_text = data
    # Generate image (this returns a PIL.Image.Image in huggingface_hub InferenceClient)
    image = client.text_to_image(
        prompt=prompt_text,
        model="black-forest-labs/FLUX.1-schnell",
    )

    return image