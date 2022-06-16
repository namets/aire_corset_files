# Main program

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests
import json
from kivy.logger import Logger
from jnius import autoclass
import jnius
from kivy import platform

from android.permissions import request_permissions, Permission
request_permissions([Permission.INTERNET, Permission.BLUETOOTH, Permission.BLUETOOTH_ADMIN])


BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
BluetoothServerSocket = autoclass('android.bluetooth.BluetoothServerSocket')
UUID = autoclass('java.util.UUID')
InputStreamReader = autoclass('java.io.InputStreamReader')
BufferedReader = autoclass('java.io.BufferedReader')
System = autoclass('java.lang.System')
kivy.require('2.1.0')

# Build app
class MyApp(App):
    def build(self):
        return ButtonApp()
  
# Build visuals and layouts
class ButtonApp(BoxLayout):
    def __init__(self):
        super(ButtonApp, self).__init__()
    
    # Function that actually runs the content of the app
    def pressed(self):
        text = 'Data uploaded!'
        firebase_url = "https://airecorset-default-rtdb.europe-west1.firebasedatabase.app/.json"
        UUIDAdress = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
        # json_data = '{"sensor_1": 3.01, "sensor_2": 1.98}' # TEST
        
        
        blueAdapt = BluetoothAdapter.getDefaultAdapter()
        self.rfsocket = self.device.createRfcommSocketToServiceRecord(UUID.fromString(UUIDAdress))
        if self.get_port_connect():
            reader = InputStreamReader(self.rfsocket.getInputStream(), 'US-ASCII')
            recv_stream = BufferedReader(reader, 8192)
            # send_stream = self.rfsocket.getOutputStream() # No sending
            lines = [recv_stream.rstrip() for line in recv_stream]
            array_length = len(lines)
            for i in range(array_length):
                row = lines[i]
                rowlist = row.strip('][').split(', ')

                # Assign each parameter to the correct value and create a BSON array
                breath = rowlist[0]
                pressure = rowlist[1]
                worn = rowlist[2]
                json_data = '{"breath" : '+breath+', "pressure": '+pressure+', "worn" : '+worn+'}'
                res = requests.post(url=firebase_url, json=json.loads(json_data))
                self.main_text.text = text

    
    def get_port_connect(self):
        try:
            if self.rfsocket.port <= 0:
                self.rfsocket = self.device.createRfcommSocket(1) #set the port explicitly
                if not self.rfsocket.connected:
                    self.rfsocket.connect()
            else:
                if not self.rfsocket.connected:
                    self.rfsocket.connect()
            if self.rfsocket.connected:
                self.main_text.text = '[b]Connected[/b]'
            return True
        except jnius.jnius.JavaException as e:
            self.main_text.text = '[b]Cannot connect to socket[/b]'            
        


# Run the app
if __name__ == "__main__":
    app = MyApp()
    app.run()




# Test ESP
# 78:E3:6D:19:26:7A 
# 4D275F63-D439-BE85-A8BC-BA5BB09C3E30 

# Live ESP
# 6E400001-B5A3-F393-E0A9-E50E24DCCA9E