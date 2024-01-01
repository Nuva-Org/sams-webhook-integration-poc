from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List

app = FastAPI()

security = HTTPBasic()

# Hardcoded username and password for testing purposes
API_KEY = "test-api-key"


def verify_api_key(api_key: str = Header(..., convert_underscores=False)):
    if api_key != f"Api-Key {API_KEY}":
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return api_key

@app.post("/sams-testing-hook")
async def receive_webhook(payload: dict, api_key: str = Depends(verify_api_key)):
    print("Received webhook payload:", payload)
    return {"status": "Webhook received successfully"}