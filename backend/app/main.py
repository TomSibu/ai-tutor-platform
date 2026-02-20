from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Tutor Platform API",
    description="Full Virtual Teacher Backend",
    version="1.0.0"
)

# CORS for frontend connection (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Tutor Backend Running Successfully 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}