import serial
ser = serial.Serial('COM21', 9600)


def move(direction):
    if(direction == "right"):
        val = val.encode('utf-8')
        ser.write("2")
    if(direction == "left"):
        val = val.encode('utf-8')
        ser.write("3")
    else:
        val = val.encode('utf-8')
        ser.write("1")