# SEC EDGAR Client

This project provides a Python command-line tool to look up a company's CIK (Central Index Key) and retrieve the latest 10-Q or 10-K filings from the SEC EDGAR system.

## Features
- Lookup CIK by ticker symbol
- Retrieve the latest 10-Q (quarterly) or 10-K (annual) filing for a company
- Print the direct URL to the filing document
- (Optional) Download the filing document as HTML

## Requirements
- Python 3.7+
- `requests` library (install with `pip install requests`)

## Usage
1. Open a terminal and navigate to the project directory:
   ```sh
   cd "C:\Users\tejir\Downloads\GEN AI"
   ```
2. Run the script with the ticker and form type:
   ```sh
   python sec_edgar_client.py AAPL 10-Q
   ```
   or (on Windows):
   ```sh
   py sec_edgar_client.py AAPL 10-Q
   ```
   This will print the latest 10-Q URL for Apple (AAPL).

3. To download the document, uncomment the download lines in the script.

## How it Works
- The script loads a mapping of ticker symbols to CIKs from the SEC.
- It fetches the company's recent filings and finds the latest 10-Q or 10-K.
- It constructs the direct URL to the filing document and prints it.

## Example Output
```
Latest 10-Q for AAPL (CIK 0000320193):
https://www.sec.gov/Archives/edgar/data/320193/000032019325000057/aapl-20250329.htm
```

## Notes
- The script uses a custom User-Agent as required by the SEC's fair access policy.
- You can use any valid ticker symbol and form type (e.g., 10-K, 10-Q).

## License
This project is provided for educational purposes. 