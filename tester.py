import requests

# This is our endpoint
url = "http://127.0.0.1:5000/api/search"

# Pass our parameters to the endpoint
params = {
    "keyword": "Python",
    "dateRange": "2023-01-01 to 2023-12-31",
    "limit": 2
}

# Send a GET request to the endpoint
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON response if it was successful
    data = response.json()
    # Print the search results
    print("Search Results:")
    # This is the loop that will print the results of the search.
    for result in data["results"]:
        print(f"Title: {result['documentTitle']}")
        print(f"Snippet: {result['documentSnippet']}")
        print(f"URL: {result['documentURL']}")
        print(f"Timestamp: {result['timestamp']}\n")
# ERROR!
else:
    print(f"Error: {response.status_code}")
