import requests

def get_location():
    try:
        response = requests.get("http://ip-api.com/json", timeout=3)
        if response.status_code == 200:
            data = response.json()
            return f"{data['city']}, {data['regionName']}, {data['country']}"
    except requests.RequestException:
        pass
    return "Unknown"
