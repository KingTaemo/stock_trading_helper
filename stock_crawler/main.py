from stock_price import get_stock_price
from stock_news import get_stock_news

news = get_stock_news("삼성전자")
for title, link in news:
    print(f"- {title}\n  {link}")

print("삼성전자 현재가:", get_stock_price("005930.KS"))  # 코스피 종목은 .KS 붙임