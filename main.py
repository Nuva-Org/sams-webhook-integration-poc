from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List

app = FastAPI()

security = HTTPBasic()

# Hardcoded username and password for testing purposes
API_KEY = "test-api-key"


def verify_api_key(Authorization: str = Header(..., convert_underscores=False)):
    if Authorization != f"Api-Key {API_KEY}":
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Authorization

@app.post("/")
async def receive_webhook(payload: dict, Authorization: str = Depends(verify_api_key)):
    print("Received webhook payload:", payload)
    return {"status": "Webhook received successfully"}