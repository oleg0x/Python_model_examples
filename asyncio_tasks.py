import asyncio



async def func(delay, what):
    await asyncio.sleep(delay)
    print(what)



async def main():
    task1 = asyncio.create_task(func(2, 'Hello'))
    task2 = asyncio.create_task(func(3, 'World!'))
    await task1
    await task2



asyncio.run(main())
