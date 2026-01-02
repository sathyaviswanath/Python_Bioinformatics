import requests

# url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
url = "https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28insulin%29"
response = requests.get(url)
print(response.json)
