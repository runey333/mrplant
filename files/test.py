import asyncio
from bleak import BleakClient, BleakScanner

address = "c0:98:e5:49:00:03"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"

async def main(address):

    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main(address))