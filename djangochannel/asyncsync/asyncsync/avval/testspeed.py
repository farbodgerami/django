# pip install requests-async
import requests_async as requests
import asyncio
import time

baseurl='http://127.0.0.1:8000/az/1'

async def main():
    start=time.time()
    print(start)
    # for i in range(10):
    #     # print(i)
    #     response=await requests.get(baseurl)
    response=await requests.get('http://127.0.0.1:8000/az/1/')
    response=await requests.get('http://127.0.0.1:8000/az/2/')
    response=await requests.get('http://127.0.0.1:8000/az/3/')
    response=await requests.get('http://127.0.0.1:8000/az/4/')
    response=await requests.get('http://127.0.0.1:8000/az/5/')

    end=time.time()
    print(round(end-start,3))
    print('done')


asyncio.run(main())
