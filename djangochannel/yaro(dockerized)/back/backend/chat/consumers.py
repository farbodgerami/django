# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from django.http import HttpResponse
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        print(self.channel_name)#specific.bf41315cba7d4aad85034b1c5ec67807!6deb3cdcf1bf497e9c709c432dcd178e
        print(self.channel_layer)#RedisChannelLayer(hosts=[{'host': '127.0.0.1', 'port': 6379}])
        print(self.channel_layer_alias)#default
        print(self.channel_receive)#functools.partial(<bound method RedisChannelLayer.receive of <channels_redis.core.RedisChannelLayer object at 0x000001461CAAB610>>, 'specific.bf41315cba7d4aad85034b1c5ec67807!6deb3cdcf1bf497e9c709c432dcd178e')
        self.roomname=self.scope['url_route']['kwargs']['roomname']
        self.roomgroupname=f'chat_{self.roomname}'  
     
      
        await self.accept()
        
        await self.channel_layer.group_add(
            self.roomgroupname,self.channel_name
        )



    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.roomgroupname,self.channel_name)

    async def receive(self, text_data):
        print('recieve',text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']


        await self.channel_layer.group_send(
            self.roomgroupname,{
                'type':'chatroom_message',
                'message':message,
        
            }
        )

    async def chatroom_message(self,event):
        print(event)
        message=event['message']
       
        await self.send(text_data=json.dumps({'message':message }))