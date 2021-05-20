import asyncio

async def fetch_data(data):
    print('Start Fetching')
    await asyncio.sleep(2)
    print('Done Fetching')
    return {'data':data}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data(50))
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2

asyncio.run(main())
