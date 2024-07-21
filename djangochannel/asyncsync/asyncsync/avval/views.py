from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import asyncio
import time
import aiohttp
import requests
from asgiref.sync import sync_to_async,SyncToAsync
# (X)
@sync_to_async()
def abc(x):
    for i in range(500000):
        print(str(i)+str(x))

    # time.sleep(seconds)
# def index(request,seconds):
async def index(request,seconds):
    starttime=time.time()
    # time.sleep(1)
    # time.sleep(seconds)
    # print('a')
    # await abc(seconds)
    # for i in range(50):
    #     print('SYNC '+str(i))
 
    # for i in range(1000000):
    #     print(str(i)+str(i))
    # await asyncio.sleep(seconds)
    # result = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false')
    # print(result)
    # result = result.json()

 

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            result = await response.json()
            # result = await response.text()

            # print('dddddddddddddddddd',result)
    # endtime=time.time()
    # result=endtime-starttime
    # return HttpResponse("Done")
     
    # print('SYNC '+str(result))
    # return HttpResponse(f'you waited {result} seconds')
    return JsonResponse({"results":result})
    # return HttpResponse(f'{result}')
 
# cpu intensive in async:
# def testasync(request,seconds):
async def testasync(request,seconds):
    starttime=time.time()
    # for i in range(50000):
    #     print('ASYNC'+str(i))
    await asyncio.sleep(2)
    # time.sleep(5)
    endtime=time.time()
    result=endtime-starttime
     
    print('ASYNC'+str(result))
    return HttpResponse(f'you waited {result}seconds')

# (Y)
# async:
# async def index(request,seconds):
#     print(seconds)
#     await asyncio.sleep(seconds) 
#     print(f'{seconds} done')
#     return HttpResponse(f'you waited {seconds}seconds')

async def test(request,seconds):
    start=time.time()
    # print(start)
    await asyncio.sleep(seconds)
    # time.sleep(seconds)
    end=time.time()
    print(round(end-start,3))
    print('do3nee')
    return HttpResponse(f'you {seconds} waited seconds')


# @sync_to_async(thread_sensitive=False)
def callApi(request):
    # print("callApi:" + str(threading.get_native_id()))
    #result = result.json()
    # students = Student.objects.all()
    # print(students)
    #print(result)

    # url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as response:
    #         print("Status:", response.status)
    #         print("Content-type:", response.headers['content-type'])
    #         html = await response.json()
    return HttpResponse("Done")
def indexx(request,seconds):
    print(seconds)
    time.sleep(seconds)
    print(f'{seconds} do344ne')
    return HttpResponse(f'you waited {seconds}seconds')