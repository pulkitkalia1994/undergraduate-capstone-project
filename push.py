
#!/usr/bin/env python
import requests
import json

API_KEY = 'o.wCvncQO0ls4LNCQ6hEw1TQl7lrfzD9dk'

# Send a message to all your registered devices.
def pushMessage(title, body):
    data = {
        'type':'note', 
        'title':title,
        'body':body
        }
    resp = requests.post('https://api.pushbullet.com/api/pushes',data=data, auth=(API_KEY,''))

# Test the function:    
pushMessage("Important Notice", "Gas leakage detected and knob has been turned off")
