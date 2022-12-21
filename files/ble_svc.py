from flask import Flask
import asyncio
from bleak import BleakScanner, BleakClient, BleakError
import sys

app = Flask(__name__)

#args = parse_ble_args('Print advertisement data from a BLE device')
addr = "c0:98:e5:49:00:03"
timeout = 10.0
#handle_sigint()

moisture_level = 500
SERVICE_UUID = "790a1915-6284-4d1a-957d-23be708470bb"

async def find():
    devices = await BleakScanner.discover(timeout=timeout)
    for d in devices:
        print(d)
        #async with BleakClient(d.address) as client:
        #    model_number = await client.read_gatt_char(MODEL_NBR_UUID, timeout=5.0)
        #    print(f"Address: {d.address}")
        #    print("       Model Number: {0}".format("".join(map(chr, model_number))))


async def set_moisture_level():
    print(f"searching for device {addr} ({timeout}s timeout)")
    try:
        async with BleakClient(addr,timeout=timeout) as client:
            print("connected")
            #loop = asyncio.get_event_loop()
            #print("Current event loop from the main thread" + str(loop))
            try:
                print(client.services)
                for svc in client.services.services:
                    curr_svc = client.services.services[svc]
                    print(curr_svc.uuid)
                    print(curr_svc.description)
                    print(curr_svc.characteristics)
                    for ch in curr_svc.characteristics:
                        print(ch.uuid)
                moisture_svc = client.services.get_service(SERVICE_UUID)
                moisture_char = moisture_svc.characteristics[0]
                print(moisture_level.to_bytes(2, "little"))
                await client.write_gatt_char(moisture_char, moisture_level.to_bytes(2, "little"))
            except Exception as e:
                print(e)
            finally:
                await client.disconnect()
                print("The client has disconnected.")
    except BleakError as e:
        print("not found")

@app.route("/set/<level>", methods=['POST'])
def set_moisture(level):
    if (int(level) >= 0 and int(level) <= 700):
        global moisture_level
        moisture_level = int(level)
        asyncio.run(set_moisture_level())
        return {"result" : f"set to {moisture_level}"}
    else:
        return {"result" : f"Invalid level"}
    
@app.route("/get", methods=['GET'])
def get_moisture():
    #asyncio.run(find())
    return {"result" : str(moisture_level)}
