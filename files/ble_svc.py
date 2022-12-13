from flask import Flask
import asyncio
from bleak import BleakScanner, BleakClient, BleakError
from ble_utils import parse_ble_args, handle_sigint
import sys

args = parse_ble_args('Print advertisement data from a BLE device')
addr = args.addr.lower()
timeout = args.timeout
handle_sigint()

moisture_level = 500
SERVICE_UUID = "790a1915-6284-4d1a-957d-23be708470bb"

app = Flask(__name__)

async def find():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)
        #async with BleakClient(d.address) as client:
        #    model_number = await client.read_gatt_char(MODEL_NBR_UUID, timeout=5.0)
        #    print(f"Address: {d.address}")
        #    print("       Model Number: {0}".format("".join(map(chr, model_number))))


async def set_moisture(address, level):
    print(f"searching for device {address} ({timeout}s timeout)")
    try:
        async with BleakClient(address,timeout=timeout) as client:
            print("connected")
            loop = asyncio.get_event_loop()
            print("Current event loop from the main thread" + str(loop))
            try:
                future = asyncio.run_coroutine_threadsafe(client.write_gatt_char(SERVICE_UUID, bytes(level), loop))
            except:
                print("An error occurred")
            finally:
                await client.disconnect()
                print("The client has disconnected.")
    except BleakError as e:
        print("not found")

@app.route("/set/<level>", methods=['POST'])
def set_moisture(level):
    global moisture_level
    moisture_level = level
    set_moisture(addr, moisture_level)
    return {"result" : f"set to {moisture_level}"}
    
@app.route("/get", methods=['GET'])
def get_moisture():
    #asyncio.run(find())
    return {"result" : str(moisture_level)}
