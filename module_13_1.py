import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    strongman1 = start_strongman('Pasha', 3)
    strongman2 = start_strongman('Denis', 4)
    strongman3 = start_strongman('Apollon', 5)
    await strongman1
    await strongman2
    await strongman3


if __name__ == '__main__':
    asyncio.run(start_tournament())