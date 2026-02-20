# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "adafruit-circuitpython-ahtx0",
#     "adafruit-circuitpython-vcnl4200",
#     "adafruit-blinka",
#     "rpi-gpio>=0.7.1",
# ]
# ///
"""Lecture multi-capteurs AHT20 + VCNL4200 via I2C."""

import board
import adafruit_ahtx0
import adafruit_vcnl4200

i2c = board.I2C()
aht = adafruit_ahtx0.AHTx0(i2c)
vcnl = adafruit_vcnl4200.Adafruit_VCNL4200(i2c)

print(f"Temperature: {aht.temperature:.1f} C")
print(f"Humidite: {aht.relative_humidity:.1f} %RH")
print(f"Proximite: {vcnl.proximity}")
print(f"Lumiere: {vcnl.lux:.1f} lux")
