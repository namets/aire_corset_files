# Fetch data from the Bluetooth device txt file and pass it to the database 
import array as arr
import pymongo

# Create a connection to the MongoDB cloud
myclient = pymongo.MongoClient("url", connect = False)
mydb = myclient["sensor_data"]
mycol = mydb["sensor_data"]

# Read the contents of the test text file 
with open("testdata.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    array_length = len(lines)
    for i in range(array_length):
        row = lines[i]
        rowlist = row.strip('][').split(', ')

        # Assign each parameter to the correct value and create a BSON array
        breath = rowlist[0]
        pressure = rowlist[1]
        worn = rowlist[2]
        arr = {"breath" : breath, "pressure": pressure, "worn" : worn}

        # Insert the BSON array into the cloud
        tofind = mycol.insert_one(arr)
		