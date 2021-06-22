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


def readSerial():
    string = " "
    if serial.readable():
        string = serial.readline().decode()
    return string


while True:
    try:
        serial.write('0'.encode())

        data = readSerial()
        print(data)
        time.sleep(1)

        serial.write('1'.encode())

        data = readSerial()
        print(data)
        time.sleep(1)


    except Exception as e:
        print(e)

    finally:
        pass
