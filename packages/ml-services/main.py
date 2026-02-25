"""
Smart Traffic Platform — ML Service
Entry point for the FastAPI-based ML inference server.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Smart Traffic ML Service",
    description="Real-time vehicle detection and traffic analysis powered by YOLOv8.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health-check endpoint."""
    return {"status": "healthy", "service": "ml-service"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
