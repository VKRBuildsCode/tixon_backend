from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

import requests

origins = [
  "*"
    # Add more allowed origins as needed
]
url = 'https://zohoapis.in/backstage/v3/portals/60034569483/events'

headers = {
    'Authorization': 'Zoho-oauthtoken 1000.303564e11510ada4e4ec00a71a274b0e.af6ce52cc6c176f4b07c9d6b9e7a00e4',  # Replace with your token
}

# Make the GET request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response if needed
    data = response.json()
    print("Response Data:", data['events'][0])
else:
    print(f"Error: {response.status_code} - {response.text}")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow credentials (cookies, authorization headers)
    allow_methods=["*"],     # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],     # Allow all headers
)
@app.get("/")
async def main():
    data = response.json()
    print(str(data))
    return data['events']

















