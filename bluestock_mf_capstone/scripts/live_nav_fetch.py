import requests
import pandas as pd

# Fetch live NAV for 5 fund schemes
schemes = {
    "HDFC Top 100": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092
}

for fund_name, code in schemes.items():
    print(f"\nFetching: {fund_name}")
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data["data"])
    df["fund_name"] = fund_name
    df.to_csv(f"data/raw/nav_{code}.csv", index=False)
    print(f"Saved! Rows: {len(df)}")