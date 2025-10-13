import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime
import time


CITY_URL = "https://www.timeanddate.com/weather/ukraine/chernihiv"
UPDATE_INTERVAL = 1800
DB_NAME = "weatherdb.sl3"

def create_db():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            datetime TEXT,
            temperature REAL
        )
    ''')
    connect.commit()
    connect.close()

def get_temperature():
    response = requests.get(CITY_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    temp_element = soup.find("div", class_="h2")
    if not temp_element:
        raise Exception("Не вдалося знайти температуру на сторінці.")

    temp_text = temp_element.text.strip().replace("°C", "").strip()
    try:
        return float(temp_text)
    except ValueError:
        raise Exception(f"Невірний формат температури: {temp_text}")

def insert_weather(temp):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO weather (datetime, temperature) VALUES (?, ?)", (now, temp))
    conn.commit()
    conn.close()
    print(f"[{now}] Температура: {temp} °C — записано до БД.")

def main():
    create_db()
    print("⛅ Початок збору даних про погоду... (оновлення кожні 30 хвилин)")

    while True:
        try:
            temp = get_temperature()
            insert_weather(temp)
        except Exception as e:
            print(f"Помилка: {e}")

        time.sleep(UPDATE_INTERVAL)



if __name__ == "__main__":
    main()
