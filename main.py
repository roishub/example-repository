import requests

# Make a GET request to the API endpoint
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# Ensure the response is successful (status code 200)
assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

# Ensure the response is in JSON format
assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Expected response to be in JSON format"

# Ensure the response contains the expected data
expected_data = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
assert response.json() == expected_data, f"Expected {expected_data} but got {response.json()}"

print("All tests passed!")

