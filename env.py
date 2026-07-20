import os
token = os.getenv("API_TOKEN")
print(token)
if token is None:
    print("API key not found!")
else:
    print("API key loaded successfully.")
tokens = os.environ["API_TOKEN"]
print(tokens)
env = os.getenv("ENV" , "development")
print(env)

for key, value in os.environ.items():
    print(key, "=", value)