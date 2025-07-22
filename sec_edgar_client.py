import requests
import sys

class SECEdgarClient:
    """
    A client for retrieving company CIKs and SEC filings (10-Q, 10-K) from the SEC EDGAR system.
    """
    def __init__(self, user_agent):
        """
        Initialize the client and load the ticker-to-CIK mapping from the SEC.
        :param user_agent: A string identifying your app to the SEC (per their fair access policy).
        """
        self.user_agent = user_agent
        self.ticker_url = 'https://www.sec.gov/files/company_tickers_exchange.json'
        self.ticker_dict = self._load_ticker_dict()

    def _load_ticker_dict(self):
        """
        Loads the ticker-to-CIK mapping from the SEC. Handles multiple possible JSON structures.
        :return: Dictionary mapping ticker symbols to company info dicts.
        """
        headers = {'User-Agent': self.user_agent}
        r = requests.get(self.ticker_url, headers=headers)
        if r.status_code == 200 and 'application/json' in r.headers.get('Content-Type', ''):
            data = r.json()
            # Case 1: dict with string keys (old SEC format)
            if isinstance(data, dict) and all(isinstance(k, str) and k.isdigit() for k in data.keys()):
                ticker_dict = {}
                for entry in data.values():
                    ticker_dict[entry['ticker'].upper()] = entry
                return ticker_dict
            # Case 2: list of [columns, companies] (current format)
            elif isinstance(data, list) and len(data) == 2:
                columns = data[0]
                companies = data[1]
                ticker_dict = {}
                for entry in companies:
                    entry_dict = dict(zip(columns, entry))
                    ticker_dict[entry_dict['ticker'].upper()] = entry_dict
                return ticker_dict
            # Case 3: dict with "fields" and "data"
            elif isinstance(data, dict) and "fields" in data and "data" in data:
                columns = data["fields"]
                companies = data["data"]
                ticker_dict = {}
                for entry in companies:
                    entry_dict = dict(zip(columns, entry))
                    ticker_dict[entry_dict['ticker'].upper()] = entry_dict
                return ticker_dict
            else:
                raise Exception('Unknown SEC ticker JSON structure.')
        else:
            raise Exception('Failed to load ticker data from SEC.')

    def get_cik(self, ticker):
        """
        Get the CIK (Central Index Key) for a given ticker symbol.
        :param ticker: The stock ticker symbol (e.g., 'AAPL').
        :return: The 10-digit CIK as a string, or None if not found.
        """
        entry = self.ticker_dict.get(ticker.upper())
        if entry:
            return str(entry['cik']).zfill(10)
        return None

    def get_company_submissions(self, cik):
        """
        Fetch the company's SEC submissions JSON using its CIK.
        :param cik: The 10-digit CIK string.
        :return: JSON data of company submissions.
        """
        url = f'https://data.sec.gov/submissions/CIK{cik}.json'
        headers = {'User-Agent': self.user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception(f'Failed to fetch submissions for CIK {cik}')

    def get_latest_filing(self, cik, form_type):
        """
        Find the latest filing of a given form type (e.g., '10-Q', '10-K') for a company.
        :param cik: The 10-digit CIK string.
        :param form_type: The SEC form type to search for.
        :return: Dict with accession_number, primary_document, and form, or None if not found.
        """
        data = self.get_company_submissions(cik)
        filings = data.get('filings', {}).get('recent', {})
        forms = filings.get('form', [])
        accession_numbers = filings.get('accessionNumber', [])
        primary_docs = filings.get('primaryDocument', [])
        for i, form in enumerate(forms):
            if form == form_type:
                return {
                    'accession_number': accession_numbers[i].replace('-', ''),
                    'primary_document': primary_docs[i],
                    'form': form
                }
        return None

    def get_filing_document_url(self, cik, accession_number, primary_document):
        """
        Construct the URL to the filing document on the SEC EDGAR site.
        :param cik: The 10-digit CIK string.
        :param accession_number: The accession number for the filing (no dashes).
        :param primary_document: The filename of the primary document.
        :return: The full URL to the filing document.
        """
        return f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession_number}/{primary_document}'

    def download_document(self, url, output_path):
        """
        Download a document from the SEC and save it locally.
        :param url: The document URL.
        :param output_path: The local file path to save the document.
        :return: True if successful, False otherwise.
        """
        headers = {'User-Agent': self.user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(r.content)
            return True
        return False

if __name__ == '__main__':
    # Command-line interface for the SEC EDGAR client
    if len(sys.argv) < 3:
        print('Usage: python sec_edgar_client.py <TICKER> <FORM_TYPE>')
        print('Example: python sec_edgar_client.py AAPL 10-Q')
        sys.exit(1)
    ticker = sys.argv[1]
    form_type = sys.argv[2]
    user_agent = 'TejirSECApp/1.0 (tejir@example.com)'
    client = SECEdgarClient(user_agent)
    cik = client.get_cik(ticker)
    if not cik:
        print(f'CIK not found for ticker {ticker}')
        sys.exit(1)
    filing = client.get_latest_filing(cik, form_type)
    if not filing:
        print(f'No {form_type} found for CIK {cik}')
        sys.exit(1)
    url = client.get_filing_document_url(cik, filing['accession_number'], filing['primary_document'])
    print(f'Latest {form_type} for {ticker} (CIK {cik}):')
    print(url)
    # Uncomment to download the document
    # if client.download_document(url, f'{ticker}_{form_type}.html'):
    #     print(f'Downloaded to {ticker}_{form_type}.html')
    # else:
    #     print('Download failed.') 