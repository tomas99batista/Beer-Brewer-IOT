# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import lcddriver
import time
import Adafruit_DHT
from datetime import datetime

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio=21

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

def get_temp_hum():
    # Use read_retry method. This will retry up to 15 times to
    # get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    # Reading the DHT11 is very sensitive to timings and occasionally
    # the Pi might fail to get a valid reading. So check if readings are valid.
    if humidity is not None and temperature is not None:
        return str(temperature), str(humidity)
    else:
        print('Failed to get reading. Try again!')

max_temp = 0
time_max_temp = datetime.now()

min_temp = 123456789
time_min_temp = datetime.now()

counter = 0
total = 0
# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Writing to display")
        
        temp, hum = get_temp_hum()
        
        # MEDIA
        total += float(temp)
        counter += 1
        media = total/counter
        
        # MAX TEMP
        if float(temp) > max_temp:
            max_temp = float(temp)
            time_max_temp = datetime.now()

        # MIN TEMP
        if float(temp) > min_temp:
            min_temp = float(temp)
            time_min_temp = datetime.now()
        
        # ACTUAL TEMP
        display.lcd_display_string(f"T {temp} | H {hum}", 1) # Write line of text to first line of display
        display.lcd_display_string(f"{datetime.now()}", 2) # Write line of text to second line of display
        time.sleep(15)                                     # Give time for the message to be read
        
        # MEDIA TEMP
        display.lcd_clear()
        display.lcd_display_string(f"Media {media}", 1)  # Refresh the first line of display with a different message
        display.lcd_display_string(f"Leituras: {counter}", 2)  # Refresh the first line of display with a different message
        time.sleep(5)                                     # Give time for the message to be read

        # MAX TEMP
        display.lcd_clear()
        display.lcd_display_string(f"Max Temp {max_temp}", 1)  # Refresh the first line of display with a different message
        display.lcd_display_string(f"{time_max_temp}", 2)  # Refresh the first line of display with a different message
        time.sleep(5)                                     # Give time for the message to be read

        # MIN TEMP
        display.lcd_clear()
        display.lcd_display_string(f"Min Temp {min_temp}", 1)  # Refresh the first line of display with a different message
        display.lcd_display_string(f"{time_min_temp}", 2)  # Refresh the first line of display with a different message
        time.sleep(5)                                     # Give time for the message to be read

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
