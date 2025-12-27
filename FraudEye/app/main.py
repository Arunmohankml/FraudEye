from fastapi import FastAPI
from app.routes.transaction import router

app = FastAPI(title="FraudEye – AML Fraud Detection")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"status": "FraudEye backend running"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

