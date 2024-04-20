#!/usr/bin/python3
"""Check if Gunicorn is serving content via Flask app"""

import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/airbnb-onepage/"
    response = requests.get(url)
    if response.status_code == 200 and response.text.strip() == "Hello HBNB!":
        print("Gunicorn is serving content via Flask app successfully!")
    else:
        print("Gunicorn is not serving content correctly. Check your setup.")

