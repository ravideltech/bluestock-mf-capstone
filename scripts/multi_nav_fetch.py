import requests
import pandas as pd

codes = [119551,120503,118632,119092,120841]

for code in codes:

    url = f"https://api.mfapi.in/mf/{code}"

    data = requests.get(url).json()

    df = pd.DataFrame(data["data"])

    df.to_csv(f"data/raw/{code}.csv", index=False)

    print(code, "saved")