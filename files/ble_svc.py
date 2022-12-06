from flask import Flask
import asyncio
from bleak import BleakClient
from bleak import BleakScanner, BleakClient

app = Flask(__name__)

async def find():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)
        #async with BleakClient(d.address) as client:
        #    model_number = await client.read_gatt_char(MODEL_NBR_UUID, timeout=5.0)
        #    print(f"Address: {d.address}")
        #    print("       Model Number: {0}".format("".join(map(chr, model_number))))

@app.route("/set/<level>", methods=['POST'])
def set_moisture(level):
    return {"result" : f"set to {level}"}
    
@app.route("/get", methods=['GET'])
def get_moisture():
    asyncio.run(find())
    return {"result" : str(444)}
