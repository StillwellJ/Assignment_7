Microservice A: Search Engine Microservice
==========================================

This microservice allows users to perform keyword-based searches on a sample dataset of documents. It responds with JSON-formatted search results that include document titles, snippets, URLs, and timestamps.

Requirements
------------
- Python
- Flask

Installation
------------
1. Install flask, most likely pip install flask.

2. Run the Microservice:
   - Run the microservice.

The microservice should run on http://127.0.0.1:5000/api/search which can be accessed through your browser of choice.

Usage Instructions
------------------
How to Request Data from the Microservice
------------------------------------
Here is how to make a request to the microservice:

1. Endpoint: /api/search
2. HTTP Method: GET
3. Parameters:
   - keyword (required): The term to search within the document titles and snippets.
   - dateRange (optional): Date range for filtering results (currently not implemented).
   - limit (optional): Number of search results to return (default is 10).

Example Call to the Microservice in Python:
-------------------------
```python
import requests

url = "http://127.0.0.1:5000/api/search"
params = {
    "keyword": "Python",
    "dateRange": "2023-01-01 to 2023-12-31",
    "limit": 2
}

response = requests.get(url, params=params)
data = response.json()  # Parse JSON response
print(data)  # Outputs the search results
```
How to Receive Data from the Microservice
------------------------------------
All responses from the microservice will be in JSON format.
- results: A list of search results with each entry containing:
  - documentTitle: Title of the document.
  - documentSnippet: A short snippet or summary of the document.
  - documentURL: URL of the document.
  - timestamp: Date of the document's publication.

Example of receiving a request from the microservice in Python.
----------------------------------------
```python
if response.status_code == 200:
    data = response.json()
    for result in data["results"]:
        print(f"Title: {result['documentTitle']}")
        print(f"Snippet: {result['documentSnippet']}")
        print(f"URL: {result['documentURL']}")
        print(f"Timestamp: {result['timestamp']}\n")
else:
    print(f"Error: {response.status_code}")
```
