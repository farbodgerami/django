import  asyncio

async def test():
    n=4 
    while n!=0:
        print(n)
        n-=1
        await asyncio.sleep(1)
        

asyncio.run( test())