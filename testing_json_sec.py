import requests

class SecScraper:
    def __init__(self, fileurl):
        self.fileurl = fileurl
        self.filejson = []
        self.ticker_dict = {}

        headers = {
            'User-Agent': 'TejirSECApp/1.0 (tejir@example.com)'  # Replace with your info
        }

        # Download the JSON file
        r = requests.get(self.fileurl, headers=headers)
        print("HTTP Status Code:", r.status_code)

        if r.status_code == 200 and 'application/json' in r.headers.get('Content-Type', ''):
            self.filejson = r.json()
            print("✅ JSON data loaded successfully.\n")
            self.cik_json_to_dict()
        else:
            print("❌ Failed to load JSON. Here’s the response:")
            print(r.text)

    def cik_json_to_dict(self):
        # New format: list of dictionaries
        for entry in self.filejson:
            self.ticker_dict[entry['ticker']] = entry

    def find_ticker(self, ticker_symbol):
        return self.ticker_dict.get(ticker_symbol.upper(), None)


# ✅ Use the full list of tickers
url = 'https://www.sec.gov/files/company_tickers_exchange.json'

# 🔍 Create scraper and search for OCE
sec = SecScraper(url)
result = sec.find_ticker('OCE')

if result:
    print("\n🔎 Result for 'OCE':")
    print(result)
else:
    print("\n❌ 'OCE' not found. Example tickers:")
    print(list(sec.ticker_dict.keys())[:20])
# Example output
# HTTP Status Code: 200