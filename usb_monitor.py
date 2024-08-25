import os
import time

def get_usb_devices():
    # Runs the 'lsusb' command to list connected USB devices
    return os.popen('lsusb').read()

def display_usb_device_details():
    # Runs the 'lsusb -v' command to display detailed information about connected USB devices
    usb_details = os.popen('lsusb -v').read()
    print("Details of connected USB device(s):\n")
    print(usb_details)

def monitor_usb_connection():
    while True:
        usb_devices = get_usb_devices()
        
        if usb_devices:
            print("Connected USB device(s):\n")
            print(usb_devices)
            display_usb_device_details()
            break
        else:
            print("No USB device connected. Please connect a USB device...")
            time.sleep(5)  # Waits 5 seconds before checking again

if __name__ == "__main__":
    monitor_usb_connection()
