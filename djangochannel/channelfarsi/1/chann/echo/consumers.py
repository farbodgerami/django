from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from channels.consumer import SyncConsumer,AsyncConsumer
from asgiref.sync import async_to_sync
import json
from random import randint
from time import sleep
import urllib.parse as urlpars

class EchoConsumer(WebsocketConsumer):
    def connect(self):
        # ebe ye channel ozvesh kardim
        self.room_id = "ee"
        self.user=self.scope['user']
        # print(self.user)
        username=self.user.username
        self.scope['session']

        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_add)(
                    self.room_id,
                    self.channel_name
                )
        #     #ma too urls.py az ina dashtim: request.GET['receiver'] vase gereftane
        #     #  http://localhost:8000/chat/new/sender/?receiver=b&text=hello
        #     # hal dar inja darim:
        # var socket = new WebSocket("ws://" + window.location.host + "/ws/?name=test&version=1");
        #     print(self.scope['query_string'])#b'name=test&varsion=1'
        #     # hal bayd inaro estekhraj konim:(import urllib.parse as urlpars)
        #     fromurl=self.scope['query_string']
        # baraye estekhraje value ha az key library be name urllib estefade mikonim
        #     params=urlpars.parse_qs(fromurl.decode('UTF-8'))
        #     # print(params)#{'name': ['test'], 'varsion': ['1']}
        #     # name=params['name'][0]
        #     # version=params['varsion'][0]
        #     # chon momkene dar stringe parametr ha masalan varsion= bashe,vase inke error nade darim:
        #     version=params.get('version',[None])#inja mige agar khali bood None ro bezar
        #     name=params.get('name',[None])
        #     print(name)



            self.accept()
        else:
            self.close()
        # for i in  range(1000):
        #  self.send(json.dumps({'message':randint(1,100)}))
        #  sleep(1)
            # self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_id,self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send(text_data=text_data + " - Sent By Server")
        elif bytes_data:
            self.send(bytes_data=bytes_data)
    
    def echo_message(self, event):
        message = event['message']

        self.send(text_data=message)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['username']
        self.group_name = f"chat_{self.user_id}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name  )
      
    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_json = json.loads(text_data)
 
            username = text_data_json['receiver']
            target_group_name = f"chat_{username}"
            await self.channel_layer.group_send(
                # be in befrest:
                target_group_name,
                {
                    'type': 'chat_message',
                    'message': text_data
                }
            )
            # #  be echo befreste:
            await self.channel_layer.group_send(
                'ee',
                {
                    'type': 'echo_message',
                    'message': text_data
                }
            )

    async def chat_message(self, event):
        print(event) 
        message = event['message']
        await self.send(text_data=message)

 
