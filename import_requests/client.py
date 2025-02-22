import requests

PORT = 5000

# The URL of the server
url = f"http://localhost:{PORT}"
blog_api_url = f"{url}/api/blog"

# Check if the server is running
is_server_running = False
try:
    response = requests.get(f"{url}")
    print("------------------------------------------------------------")
    print(response.status_code)
    if response.status_code == 200:
        print("Server is running")
        is_server_running = True
    else:
        print("Server is not running")
except requests.exceptions.ConnectionError:
    print("Server is not running")
print("------------------------------------------------------------")


# Check if the server is running
if not is_server_running:
    print("Server is not running")
    exit()
else:
    print("Server is running")
    print(f"Server URL: {url}")
    print(f"Server Port: {PORT}")
    print(f"Blog API URL: {blog_api_url}")
    print()
print("------------------------------------------------------------")


# GET request
response = requests.get(f"{blog_api_url}")
print("GET response:", response.json())


# POST request
manga = {
    "title": "Fullmetal Alchemist: Brotherhood",
    "author": "Hiromu Arakawa",
    "genre": "Fantasy",
    "snippet": "FMAB",
    "body": "This is the description for this manga"
}
response = requests.post(f"{blog_api_url}", data=manga)
print("POST response:", response.json())


# DELETE request
response = requests.delete(f"{blog_api_url}/656cfa3c266c48a88cea8a1f")
print("DELETE response:", response.json())


# PUT request
manga = {
    "title": "Naruto",
    "author": "Masashi Kishimoto",
    "genre": "Fantasy",
    "snippet": "Naruto",
    "body": "This is the updated description for this manga"
}
# Update the title and Description body of the manga with ID 65737ad4790d65302aebf857
response = requests.put(f"{blog_api_url}/65737ad4790d65302aebf857", data=manga)
print("PUT response:", response.json())
print("------------------------------------------------------------")
