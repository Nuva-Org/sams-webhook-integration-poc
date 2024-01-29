# SAMS Webhook Integration POC

### Setup

1. Clone the repository:
    ```
    git clone https://github.com/Nuva-Org/sams-webhook-integration-poc.git
    ```

2. Navigate into the cloned repository:
    ```
    cd sams-webhook-integration-poc.git
    ```
3. Switch branch:
    ```
    git checkout poc-websocket
    ```
    
4. Install dependencies:
    ```
    pip install poetry
    poetry install
    poetry shell
    ```

5. Download and setup ngrok locally. Follow all the steps here at https://dashboard.ngrok.com/ after loging in.


6. Run the application:
    ```
    poe open-ngrok-tunnel
    ```

To run the frontend just replace the API key with yours API key and open the ```Frontend/index.html``` in browser.
