import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

data = requests.get(url).json()

df = pd.DataFrame(data["data"])

df.to_csv("data/raw/nav_history.csv", index=False)

print("File Saved Successfully")