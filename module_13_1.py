import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i + 1} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Паша', 5))
    task2 = asyncio.create_task(start_strongman('Денис', 6))
    task3 = asyncio.create_task(start_strongman('Геракл', 7))
    await task1
    await task2
    await task3


if __name__ == '__main__':
    asyncio.run(start_tournament())