from pyngrok import ngrok

def open_ngrok_tunnel():
    # Open a ngrok tunnel
    public_url = ngrok.connect(9000)  # Assumes FastAPI server is running on port 8000
    print("ngrok tunnel is live at:", public_url)
    return public_url

def close_ngrok_tunnel():
    # Close the ngrok tunnel
    ngrok.disconnect()
local_debug = False
if __name__ == "__main__":
    try:
        # Open ngrok tunnel before starting FastAPI server
        public_url = open_ngrok_tunnel()

        # Start FastAPI server using uvicorn
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)

    finally:
        # Close ngrok tunnel when the FastAPI server is stopped
        close_ngrok_tunnel()