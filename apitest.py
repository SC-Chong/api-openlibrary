import requests

# base URL for the Open Library API
# for more info of api, refer https://openlibrary.org/dev/docs/api/search
url = "https://openlibrary.org/search.json"

# Set up query parameters
params = {
    'q': 'Harry Potter',  # Search query
    'fields': 'title,author_name,ratings_count',  # Fields to return
    'limit': 20,  # Limit to 20 results
}

# Send GET request to API
response = requests.get(url, params=params)

# Initialize an empty list
collection = []

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON data
    data = response.json()

    # Loop through the results and append relevant fields to the collection
    if 'docs' in data:
        for book in data['docs']:
            book_data = [
                book.get('title', 'No title'),
                book.get('author_name', 'No author'),
                book.get('ratings_count', 'No rating count')
            ]
            collection.append(book_data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)


print(collection)