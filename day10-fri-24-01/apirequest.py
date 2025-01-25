import requests

token = "bc6e5bd51ae334ac6e44824dc860031a56256635"
airq_api_url = "https://api.waqi.info/feed/#city#/?token=#token#"

request_url = airq_api_url.replace("#city#", "bangkok").replace("#token#", token)

response = requests.get(request_url)
json_data = response.json()['data']
print(f"{json_data['city']['name']} has current AQI of {json_data['aqi']}")