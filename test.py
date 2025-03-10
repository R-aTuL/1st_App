import requests

url = "http://127.0.0.1:5000/embed-store"
headers = {"Content-Type": "application/json"}
data = {"url": "https://dev.to/bobur/how-to-build-a-custom-gpt-enabled-full-stack-app-for-real-time-data-38k8"}

response = requests.post(url, json=data, headers=headers)
print(response.json())  # Should return success message
