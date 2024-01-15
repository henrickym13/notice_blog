import requests

class NewsApi():
    
    def __init__(self):
        self.api_key = 'your API Key here'


    def api_request(self):
        website =f'https://newsapi.org/v2/top-headlines?country=br&apiKey={self.api_key}'

        response = requests.get(website)
        api_data = response.json()
        api_data = api_data['articles']

        return api_data


    def api_request_theme(self, category):
        website =f'https://newsapi.org/v2/top-headlines?country=br&category={category}&apiKey={self.api_key}' 

        response = requests.get(website)
        api_data = response.json()
        api_data = api_data['articles']

        return api_data  