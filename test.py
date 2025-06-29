import requests

def scrap_url():
    web_url = input("Enter the website URL: ")
    embed_url = "http://127.0.0.1:5000/embed-store"
    headers = {"Content-Type": "application/json"}
    data = {"url": web_url}
    
    response = requests.post(embed_url, json=data, headers=headers)
    print(response.json())

    # Chat loop
    while True:
        query = input("Enter your question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        query_url = "http://127.0.0.1:5000/handle-query"
        data1 = {
                "question": query,
                "url":web_url}
        print(data1)
        response = requests.post(query_url, json=data1, headers=headers)
        print(response.json())

scrap_url()
