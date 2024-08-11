# run this with self signed certs:
# $ export REQUESTS_CA_BUNDLE="$(mkcert -CAROOT)/rootCA.pem" python events.py


import requests
import sseclient

# URL of the SSE server
url = 'https://sensorbox.local/events'

# Establish a streaming request to the SSE server
response = requests.get(url, stream=True)

# Wrap the response in an SSE client
client = sseclient.SSEClient(response)

# Listen to events
for event in client.events():
    print(f"Event ID: {event.id}")
    print(f"Event: {event.event}")
    print(f"Data: {event.data}")
    print("----------------------------")
