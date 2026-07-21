import logging
import requests
import subprocess
import json
import os
with open ("servers.txt" , "r") as f:
    servers = f.read().splitlines()
logging.basicConfig(level=logging.INFO)
logging.info("start of execution")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response.status_code)
except requests.RequestException as e:
    print(e)

process = subprocess.run(['git', 'status'], capture_output = True, text = True)
print(process.stdout)
with open("servers.json" , "w") as f:
    json.dump(servers, f)
text = json.dumps(servers)
token=os.getenv("API_TOKEN")
print(token)