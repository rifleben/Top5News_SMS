import requests


def search_and_return(search_term):
    """Search News API and Return Result"""
    API_KEY = "YOUR_API_KEY"

    url = ('https://newsapi.org/v2/everything?')
    parameters = {
        "apiKey": API_KEY,
        "q": f"{search_term}",
        "pageSize": 5,
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()

    articles = response.json()["articles"]

    message = [f"Here are the top {len(articles)} headlines about {search_term} \n"]
    for article in articles:
        message.append(f"\n{article['title']}")
        message.append(f"\n{article['url']}")
        message.append("\n")

    return "".join(message)
