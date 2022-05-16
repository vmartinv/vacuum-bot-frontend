import requests
import json
from app_secrets import BACKEND_URL, TOKEN

def call_service(direction):
    url = f"{BACKEND_URL}/api/services/vacuum/send_command"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "content-type": "application/json",
    }
    data = json.dumps({
        'entity_id': 'vacuum.robovac',
        'command': 'direction',
        'params': direction,
    })
    return requests.post(url, headers=headers, data=data)
