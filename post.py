import requests
from requests.auth import HTTPBasicAuth
import pyotp
import hashlib
import base64

email = "example.12@gmail.com"

secret = email + "LKJLKJSLKDJSSD"

# Encode the secret using base32 and remove padding characters
base32_secret = base64.b32encode(secret.encode()).decode().rstrip('=')

# Create a TOTP object with the secret key, 30-second interval, and SHA-512 hash function
totp = pyotp.TOTP(base32_secret, interval=30, digits=10, digest=hashlib.sha512)

# Generate the current TOTP password
password = totp.now()

print("Email:", email)
print("Secret:", secret)
print("Base32 Secret:", base32_secret)
print("Your TOTP password is:", password)

url = "https://........"
payload = {
  "github_url": "https://......",
  "contact_email": email,
  "solution_language": "python"
}

headers = {
  "Content-Type": "application/json"
}
auth = HTTPBasicAuth(email, password)

response = requests.post(url, json=payload, headers=headers, auth=auth)
print(response.status_code)
print(response.text)
