from fastapi import FastAPI, Depends, HTTPException, Header, WebSocket, WebSocketDisconnect, WebSocketException
from fastapi.security import HTTPBasic
import json
import asyncio

app = FastAPI()

security = HTTPBasic()

# Hardcoded username and password for testing purposes
API_KEY = "test-api-key"

# Store WebSocket connections
websockets = set()

def verify_api_key(Authorization: str = Header(..., convert_underscores=False)):
    if Authorization != f"Api-Key {API_KEY}":
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Authorization

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websockets.add(websocket)
    try:
        while True:
            # Keep the connection alive
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        websockets.remove(websocket)

async def send_payload_to_frontend(payload: dict):
    payload_json = json.dumps(payload)
    for websocket in websockets:
        try:
            await websocket.send_text(payload_json)
        except Exception as e:
            print("exception occured: ",e)
        

@app.post("/")
async def receive_webhook(payload: dict, Authorization: str = Depends(verify_api_key)):
    print("Received webhook payload:", payload)
    # Send payload to connected frontends
    await send_payload_to_frontend(payload)
    return {"status": "Webhook received successfully"}

@app.get("/")
async def get_websockets():
    return {"websockets": len(websockets)}