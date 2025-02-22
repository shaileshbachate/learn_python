import requests
import time

def check_internet():
    url = "https://www.google.com"
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("Internet connection not available")
    return False

print(check_internet())

counter = 0
while not check_internet():
    counter += 1
    print(f"Internet connection not available. Retrying... ({counter})")
    time.sleep(30)
print("Internet connection available")

