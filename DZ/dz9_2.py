import requests
import sqlite3
import datetime

DB_NAME = "uah_pln.db"

def create_db():
    connect = sqlite3.connect(DB_NAME)
    c = connect.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS uah_pln_rate (
            date TEXT,
            rate REAL
        )
    """)
    connect.commit()
    connect.close()

def fetch_uah_to_pln_rate():
    url = "https://api.nbp.pl/api/exchangerates/rates/a/uah/?format=json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    rate = data["rates"][0]["mid"]
    return rate

def save_rate(rate):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO uah_pln_rate (date, rate) VALUES (?, ?)", (now, rate))
    conn.commit()
    conn.close()
    print(f"[{now}] Saved UAH→PLN rate: {rate}")

class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate
    def convert_uah_to_pln(self, amount_uah):
        return amount_uah * self.rate

def main():
    create_db()
    try:
        rate = fetch_uah_to_pln_rate()
        print(f"Current UAH→PLN rate: {rate}")
        save_rate(rate)
    except Exception as e:
        print(f"Error fetching rate: {e}")
        return
    converter = CurrencyConverter(rate)
    try:
        amount = float(input("Enter amount in UAH: "))
        result = converter.convert_uah_to_pln(amount)
        print(f"{amount:.2f} UAH = {result:.2f} PLN")
    except ValueError:
        print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main()
