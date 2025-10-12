import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

url = "https://api.binance.com/api/v3/klines"
params = {
    "symbol": "BTCUSDT",
    "interval": "5m",
    "limit": 1000
}
csv_file = "btc_1year_5min.csv"

if os.path.exists(csv_file):
    print("✅ Loading saved data from CSV...")
    df = pd.read_csv(csv_file, parse_dates=["open_time"])
else:
    print("📡 Fetching data from Binance...")
    candles = []
    end_time = int(pd.Timestamp.now().timestamp() * 1000)
    ms_in_5min = 5 * 60 * 1000
    total_candles = 365 * 24 * 12
    for i in range(0, total_candles, 1000):
        start_time = end_time - (i + 1000) * ms_in_5min
        params["startTime"] = start_time
        response = requests.get(url, params=params)
        data = response.json()
        candles = data + candles
    df = pd.DataFrame(candles, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "num_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ])
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df["close"] = df["close"].astype(float)
    df.to_csv(csv_file, index=False)
    print("💾 Data saved to:", csv_file)

plt.figure(figsize=(12, 6))
plt.plot(df["open_time"], df["close"], label="BTC/USDT (5m)")
plt.title("Bitcoin Price - Last 1 Year (5 min candles)")
plt.xlabel("Date")
plt.ylabel("Price (USDT)")
plt.legend()
plt.grid(True)
plt.show()
