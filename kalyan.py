import json

# Sample JSON data (as a dictionary)
json_data = '''
{
    "name": "John",
    "age": 30,
    "action": "run"
}
'''

# Parse the JSON data
data = json.loads(json_data)

# Check if the key 'action' exists in the dictionary
if 'action' in data:
    # If the key exists, do this
    print(f"Action found: {data['action']}")
else:
    # If the key does not exist, do that
    print("No action specified.")
