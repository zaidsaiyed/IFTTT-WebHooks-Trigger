import requests, keys

key = keys.get_key()
event_name = "test_event"

ifttt_webhook_url = "https://maker.ifttt.com/trigger/" + event_name + "/with/key/" + key

# Send a POST request to the IFTTT webhook URL with the trigger data
response = requests.post(ifttt_webhook_url)

# Check the response status code to ensure the request was successful
if response.status_code == 200:
    print("IFTTT trigger sent successfully")
else:
    print("Failed to send IFTTT trigger")