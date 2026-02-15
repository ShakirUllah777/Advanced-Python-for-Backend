''''
This is used to run the task multiple while the other task in waiting for the i/o
'''

import time
import asyncio
def task():
    print('start')
    time.sleep(5)
    print('end')

task()
print('Done')

async def task():
    print("Start")
    await asyncio.sleep(3)
    print("End")

asyncio.run(task())

async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(2)
    print("Data received")

async def main():
    await asyncio.gather(
        fetch_data(),
        fetch_data(),
        fetch_data()
    )

asyncio.run(main())
