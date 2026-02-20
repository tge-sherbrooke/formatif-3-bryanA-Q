# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "adafruit-circuitpython-ahtx0",
#     "adafruit-blinka",
#     "rpi-gpio>=0.7.1",
# ]
# ///
"""Lecture du capteur AHT20 via I2C avec logique de retry."""

import board
import adafruit_ahtx0
import time

MAX_RETRIES = 3

def read_aht20():
    """Lit le capteur AHT20 avec retry en cas d'erreur."""
    i2c = board.I2C()
    sensor = adafruit_ahtx0.AHTx0(i2c)

    for attempt in range(MAX_RETRIES):
        try:
            temperature = round(sensor.temperature, 1)
            humidity = round(sensor.relative_humidity, 1)
            return temperature, humidity
        except Exception as e:
            print(f"Tentative {attempt + 1}/{MAX_RETRIES}: {e}")
            time.sleep(1)

    raise RuntimeError(f"Echec apres {MAX_RETRIES} tentatives")

def main():
    temp, humidity = read_aht20()
    print(f"Temperature: {temp} C")
    print(f"Humidite: {humidity} %RH")

if __name__ == "__main__":
    main()
