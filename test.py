import requests

# url = "http://127.0.0.1:5000/embed-store"
# headers = {"Content-Type": "application/json"}
# data = {"url": "https://dev.to/bobur/how-to-build-a-custom-gpt-enabled-full-stack-app-for-real-time-data-38k8"}

url = "http://127.0.0.1:5000/handle-query"
headers = {"Content-Type": "application/json"}
data = {"question":"Why do we provide ChatGPT with a custom knowledge base?"}

response = requests.post(url, json=data, headers=headers)
print(response.json())


# import os
# from dotenv import load_dotenv

# load_dotenv()
# model_name = os.getenv("OLLAMA_MODEL", "mistral")

# import ollama
# response = ollama.chat(model=model_name, messages=[{"role": "user", "content": "Test"}])
# print(response)
