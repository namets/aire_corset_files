# Main program

# Fetch data from the Bluetooth device txt file and pass it to the database 
import array as arr
import pymongo
# import bluetooth 
# print(bluetooth.discover_devices(lookup_names = True))
from bgapi.module import BlueGigaServer
address = "78:E3:6D:19:26:7A"
PORT = "COM3"
ble_server = BlueGigaServer(port=PORT, baud=115200, timeout=0.1)
print(ble_server.read_by_handle)
print(ble_server.ble_rsp_attributes_read)
print(ble_server.scan_responses)



# Sources
# https://appdividend.com/2022/01/21/how-to-convert-python-string-to-list/#:~:text=To%20convert%20string%20to%20list%20in%20Python%2C%20use%20the%20string,stores%20them%20in%20the%20list.
# https://www.w3schools.com/python/python_mongodb_insert.asp
# https://www.mongodb.com/community/forums/t/pymongo-errors-serverselectiontimeouterror-with-atlas-even-when-added-to-network-access/115333

# 78:E3:6D:19:26:7A