from django.shortcuts import render
from django.http import HttpResponse
import asyncio
import time


def index(request,seconds):
# async def index(request,seconds):
    starttime=time.time()
    # time.sleep(seconds)
    # await asyncio.sleep(seconds)
    # time.sleep(10)
    # print('a')
    # await abc(seconds)
    x=0
    for i in range(500000):
        print(str(i))
        x=x+1
    # await asyncio.sleep(5)
    # result = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false')
    # result = result.json()

 

    # url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as response:
    #         print("Status:", response.status)
    #         print("Content-type:", response.headers['content-type'])
    #         result = response.text()

    #         print(result)
    endtime=time.time()
    result=endtime-starttime
    # return HttpResponse("Done")
     
    print('SYNC '+str(result))
    return HttpResponse(f'you waited {result} seconds')

def index2(request,seconds):
    starttime=time.time()
    x=0
    for i in range(3200):
        print(str(i))
        x=x+1
 
    endtime=time.time()
    result=endtime-starttime
    print('SYNC '+str(result))
    return HttpResponse(f'you waited {result} seconds')


# 161x