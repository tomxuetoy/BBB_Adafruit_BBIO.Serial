import Adafruit_BBIO.UART as UART
import serial

UART.setup("UART1")

ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
    print "Serial is open!"
    ser.write("Hello World!")
    ser.close()

# Eventually, you'll want to clean up, but leave this commented for now,
# as it doesn't work yet
#UART.cleanup()
