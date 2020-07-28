import aiohttp
import asyncio
try:
    list = []
    async def fetch_agent(agent):
        async with aiohttp.ClientSession() as session:
            async with session.post(agent['url'],json=agent['payload']) as response:
                list.append(await response.json())
    print('main thread')
    event_loop = asyncio.get_event_loop()
    agents = ["https://httpbin.org/post","https://httpbin.org/post","https://httpbin.org/post","https://httpbin.org/post"]
    coroutines = [fetch_agent({'url' : agents[i], 'payload': {'id': 1, 'name': 'test'}}) for i in range(len(agents))]
    results = event_loop.run_until_complete(asyncio.gather(*coroutines,return_exceptions=True))
    for res in list:
        print(type(res),res['data'])
    print('main thread ended')
except (aiohttp.web.HTTPException) as aioHttpException:
    print(aioHttpException)
except Exception as e:
    print(e)
