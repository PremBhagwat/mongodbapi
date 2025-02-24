from fastapi import FastAPI
from routes import router
import uvicorn
app = FastAPI()

#call router api from routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Blog API"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

