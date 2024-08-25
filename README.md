How it works:
get_usb_devices(): This function executes the lsusb command to list all connected USB devices and returns the result.
display_usb_device_details(): This function executes lsusb -v to retrieve and display detailed information about all connected USB devices.
monitor_usb_connection(): This function continuously monitors for USB devices.
If no device is connected, it prompts the user to connect one and checks again every 5 seconds.
When a device is detected, it lists the connected devices and displays detailed information about them, then stops monitoring.

Expected Behavior:
If no USB device is connected, the script will display a message asking you to connect a device and will recheck every 5 seconds.
Once a USB device is connected, the script will show a list of connected devices and provide detailed information about each one, such as transfer speed, port number, and other technical details.
