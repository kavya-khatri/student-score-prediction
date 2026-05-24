import requests
import time

URL = "http://127.0.0.1:5000"

while True:
    try:
        response = requests.get(URL)

        if response.status_code == 200:
            print("Application is running successfully")
        else:
            print("Application returned an error")

    except Exception as e:
        print("Application is DOWN")
        print("Error:", e)

    print("-" * 40)

    time.sleep(10)