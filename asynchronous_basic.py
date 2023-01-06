import asyncio


async def send_second():
    n = 0
    while True:
        await asyncio.sleep(1)
        n += 1
        if n%3 == 0:
            pass
        else:
            print(f'Прошло {n} секунд(ы)')

async def send_three_second():
    n = 0
    while True:
        await asyncio.sleep(3)
        n += 3
        print(f'С момента запуска прошло {n} секунд')

async def main():
    task_1 = asyncio.create_task(send_second())
    task_2 = asyncio.create_task(send_three_second())
    await task_1
    await task_2

if __name__ == '__main__':
    asyncio.run(main())
