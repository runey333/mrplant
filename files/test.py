import asyncio
from bleak import BleakClient, BleakScanner

address = "c0:98:e5:49:00:03"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"

async def main(address):

    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

    # async with BleakClient(address) as client:
    #     model_number = await client.read_gatt_char(MODEL_NBR_UUID)
    #     print("Model Number: {0}".format("".join(map(chr, model_number))))

asyncio.run(main(address))