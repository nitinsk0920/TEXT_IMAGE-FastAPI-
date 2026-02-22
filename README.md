# 🖼️ Text-to-Image Generation API (FastAPI + Streamlit) <br>

A modular Text-to-Image generation system built using:<br>
FastAPI (Model Serving API)<br>
Streamlit (Frontend UI)<br>
Hugging Face Inference API<br>
Stable Diffusion / FLUX Model<br>
The application takes a text prompt from the user and generates an image using a hosted diffusion model.<br>

## 🚀 Features

🧠 Uses Hugging Face InferenceClient<br>
🎨 Generates images from text prompts<br>
⚡ FastAPI backend for production-ready model serving<br>
🌐 Streamlit frontend for user interaction<br>
📦 Modular project structure<br>
⬇️ Download generated image as PNG<br>
🏥 Health check endpoint<br>

## 🏗️ Tech Stack<br>

Python<br>
FastAPI<br>
Streamlit<br>
Hugging Face Hub<br>
Pillow (PIL)<br>
Pydantic<br>
python-dotenv<br>

### Model used:<br>
black-forest-labs/FLUX.1-schnell<br>

## 🔐 Environment Variables<br>


Create a .env file:
HF_TOKEN=your_huggingface_token_here<br>

Get token from:
https://huggingface.co/settings/tokens

### ⚠ Never push .env to GitHub.<br>
Add to .gitignore:


## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository<br>
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name<br>
### 2️⃣ Create Virtual Environment<br>
python -m venv venv

Activate:<br>
Windows:
venv\Scripts\activate

Mac/Linux:
2️⃣ Create Virtual Environment
source venv/bin/activate<br>

### 3️⃣ Install Dependencies<br>
pip install -r requirements.txt

If no requirements file:<br>
pip install fastapi uvicorn streamlit requests pillow python-dotenv huggingface_hub pydantic<br>

## ▶️ Running the Application<br>
Step 1: Start FastAPI Backend
uvicorn txt_image_fastapi:app --reload --port 8000<br>


API will run at:

http://localhost:8000

Test health endpoint:

http://localhost:8000/health

streamlit run app.py
<br>

Open in browser:

http://localhost:8501

### 🔁 How the System Works

User enters text prompt in Streamlit<br>
Streamlit sends POST request to FastAPI /predict<br>
FastAPI calls predict_output() from model.py<br>
Hugging Face InferenceClient generates image<br>
Image is streamed back as PNG<br>
Streamlit displays and allows download<br>


### 📡 API Endpoints
GET /

Returns API welcome message

GET /health

Returns:

{
  "status": "OK",
  "version": "stable-diffusion-xl-base-1.0"
}
POST /predict

Request body:

{
  "prompt": "A futuristic city at sunset"
}

Response:

PNG image stream


## 🛠 Future Improvements

Add async inference<br>

Add rate limiting<br>

Add authentication<br>

Deploy FastAPI on cloud (Render / AWS / GCP)<br>

Deploy Streamlit frontend publicly<br>

Use React for better frontend<br>

Add prompt history logging<br>


Add model selection dropdown<br>
