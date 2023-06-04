from flask import request
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='d1f5a77777e44122a6de651cdd725f1b')

def news():
    # Fetch top news articles
    top_headlines = newsapi.get_top_headlines(language='en', page_size=5)

    # Extract relevant information from the response
    articles = top_headlines['articles']
    news_list = [{'title': article['title'], 
    'description': article['description'],
    'url': article['url'],
    'image': article['urlToImage']} for article in articles]

    display_sidebar = True
    if request.path in ['/login', '/register']:
        display_sidebar = False
    return dict(news_list=news_list, display_sidebar=display_sidebar)
    
if __name__ == "__main__":
    news()