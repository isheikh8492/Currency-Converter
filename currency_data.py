import urllib.request
import json

with urllib.request.urlopen(
        "http://data.fixer.io/api/latest?access_key=2179433ad61d935639f9bc75e180bdf0&format=1") as url:
    json_data = json.loads(url.read().decode())

live_curr_data = json_data["rates"]
