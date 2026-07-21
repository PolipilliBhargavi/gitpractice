import requests
import logging
import os
import subprocess
process = subprocess.run(["docker", "ps"], capture_output = True, text = True)
print(process.stdout)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/health.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
try:
    response = requests.get(os.getenv("HEALTH_URL"))
    print(os.getenv("HEALTH_URL"))
    response.raise_for_status()
    data= response.json()
    if data.get("status") == "UP":
        print("Application is Healthy")
        logging.info("SUCCESS")
    else:
        print("Application is Down")
        logging.info("SUCCESS")
except requests.RequestException as e:
     print(f"Error: {e}")
     print("Application is Down")

    
