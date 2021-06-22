#!/usr/bin/python3
import time
import serial


serial = serial.Serial(
    port='/dev/ttyTHS1',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

# Wait a second to let the port initialize
time.sleep(1)

try:
    while True:
        serial.write('0'.encode())
        time.sleep(1)
        serial.write('1'.encode())
        time.sleep(1)

except Exception as e:
    print(e)

finally:
    pass
