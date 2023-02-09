import serial


while True:
    port = "COM3"
    ser = serial.Serial(port, 115200, timeout=0.050)


    inpt = input(str("INPUT: "))

    ser.write(bytearray(inpt, 'ascii'))
    print(ser.readline().decode('ascii'))

    ser.close()
