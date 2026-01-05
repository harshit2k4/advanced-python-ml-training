# this demonstrates a simple web scraping
import requests

url = "https://www.google.com"
res = requests.get(url)

print(res.status_code)

with open("google.html", "w") as file:
    file.write(res.text)

print("DONE")