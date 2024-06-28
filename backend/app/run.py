import uvicorn
from main import app

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        reload=True  # Enables auto-reloading in development mode
    )
