import serial
import time

# Arduino bilan bog'lanish
#arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Arduino'ni ishga tushirish uchun vaqt

def turn_off_arduino():
    pass
    #arduino.write(b'OFF')  # Arduino'ga "OFF" komandasini yuborish
    #time.sleep(1)  # Arduino'ni o'chirish uchun kutish
