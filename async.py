import asyncio
import time

# working around asynchronous call instead of sleep in ohlc_exchanges.py
@asyncio.coroutine
def sleepy():
    print("before sleep", time.time())
    yield from asyncio.sleep(5)
    print("after sleep", time.time())

asyncio.get_event_loop().run_until_complete(sleepy())