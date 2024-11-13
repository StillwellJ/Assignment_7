from flask import Flask, request, jsonify

app = Flask(__name__)

# Random sample documents for the sake of testing
sample_documents = [
    {"documentTitle": "Introduction to AI", "documentSnippet": "This document introduces AI concepts.", "documentURL": "http://example.com/ai", "timestamp": "2023-05-01"},
    {"documentTitle": "Data Science Basics", "documentSnippet": "Basics of data science.", "documentURL": "http://example.com/data-science", "timestamp": "2023-05-02"},
    {"documentTitle": "Python Programming Guide", "documentSnippet": "A guide on Python programming.", "documentURL": "http://example.com/python", "timestamp": "2023-05-03"}
]

# API endpoint for our search
@app.route('/api/search', methods=['GET'])
# Function to handle the search request
def search():
    keyword = request.args.get('keyword', '').lower()
    date_range = request.args.get('dateRange', '')
    limit = int(request.args.get('limit', 10))
    
    # Filter results based on keyword and date range
    results = [doc for doc in sample_documents if keyword in doc['documentTitle'].lower() or keyword in doc['documentSnippet'].lower()]
    # This is the limit range filter. It will only show the number of results that the user wants to see.
    results = results[:limit]

    # We are returning data as a json file. Pretty easy.
    return jsonify({"results": results, "count": len(results)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
