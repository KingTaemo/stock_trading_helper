import requests
from bs4 import BeautifulSoup

def get_stock_news(query, max_count=5):
    url = f"https://search.naver.com/search.naver?where=news&query={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    news_items = soup.select("ul.list_news div.news_area a.tit")
    results = []
    for item in news_items[:max_count]:
        title = item.text.strip()
        link = item['href']
        results.append((title, link))
    return results