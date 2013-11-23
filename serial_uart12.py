import Adafruit_BBIO.UART as UART
import serial

UART.setup("UART1")
UART.setup("UART2")

# communicate between uart1 and uart2
# Check details in my wiznote...
