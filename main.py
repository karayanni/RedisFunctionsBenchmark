import asyncio
import redis.asyncio as redis
import time


keysRange = range(1000000)


async def main():
    print('Starting bombing')

    r = redis.Redis(host='localhost', port=6379)
    if await r.ping():
        print("connection succeeded")

    await asyncio.create_task(set_util(r, 'nader first set', '---------nice test---------'))

    await asyncio.create_task(get_util(r, 'nader first set'))

    await set_bomb(r)

    await asyncio.create_task(get_util(r, 'random message 1'))
    print(f'{main().__name__} done')


async def set_bomb(r):
    for i in range(500000):
        print(i)
        r.set(i, f'random message {i}')


async def set_util(r, key, val):
    # print(await r.set(key, val))
    await r.set(key, val)


async def get_util(r, key):
    print(await r.get(key))


if __name__ == '__main__':
    asyncio.run(main())
    print("test done")

