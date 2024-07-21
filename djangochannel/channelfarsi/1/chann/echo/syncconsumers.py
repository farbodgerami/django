from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from random import randint
from time import sleep
import urllib.parse as urlpars

class EchoConsumer(WebsocketConsumer):
    def connect(self):
        # ebe ye channel ozvesh kardim
        # self.room_id = "ee"
        # self.user=self.scope['user']
        # print(self.user)
        # if self.user.is_authenticated:
        #     async_to_sync(self.channel_layer.group_add)(
        #         self.room_id,
        #         self.channel_name
        #     )
        #     #ma too urls.py az ina dashtim: request.GET['receiver'] vase gereftane
        #     #  http://localhost:8000/chat/new/sender/?receiver=b&text=hello
        #     # hal dar inja darim:
        #     print(self.scope['query_string'])#b'name=test&varsion=1'
        #     # hal bayd inaro estekhraj konim:
        #     fromurl=self.scope['query_string']
        #     params=urlpars.parse_qs(fromurl.decode('UTF-8'))
        #     # print(params)#{'name': ['test'], 'varsion': ['1']}
        #     # name=params['name'][0]
        #     # version=params['varsion'][0]
        #     # chon momkene dar stringe parametr ha masalan varsion= bashe,vase inke error nade darim:
        #     version=params.get('version',[None])#inja mige agar khali bood None ro bezar
        #     name=params.get('name',[None])
        #     print(name)



        #     self.accept()
        # else:
        #     self.close()
        # for i in  range(1000):
        #  self.send(json.dumps({'message':randint(1,100)}))
        #  sleep(1)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send(text_data=text_data + " - Sent By Server")
        elif bytes_data:
            self.send(bytes_data=bytes_data)
    
    def echo_message(self, event):
        message = event['message']

        self.send(text_data=message)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # print('scopeeeeeeeeeeeeeeeeeee', self.scope)
   
     
        self.user_id = self.scope['url_route']['kwargs']['username']
        self.group_name = f"chat_{self.user_id}"
        # print( self.channel_name)# specific.cda4a732052b4fbea63a19cb8c5b8cbc!e2e979801dc64a65ac83b5cfef26e4dd
        # print('group_name',self.group_name)
        # print( self.channel_layer)#RedisChannelLayer(hosts=[{'host': '127.0.0.1', 'port': 6379}])
        # print('ggg',async_to_sync)#<class 'asgiref.sync.AsyncToSync'>
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name  )
      
    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_json = json.loads(text_data)
            # print('lllll',text_data_json)#lllll {'sender': 'a', 'receiver': 'b', 'text': 'j'}
            username = text_data_json['receiver']
            target_group_name = f"chat_{username}"
            async_to_sync(self.channel_layer.group_send)(
                # be in befrest:
                target_group_name,
                {
                    'type': 'chat_message',
                    'message': text_data
                }
            )
            # #  be echo befreste:
            # async_to_sync( self.channel_layer.group_send)(
            #     'ee',
            #     {
            #         'type': 'echo_message',
            #         'message': text_data
            #     }
            # )

    def chat_message(self, event):
        print(event)#{'type': 'chat_message', 'message': '{"sender":"aaaaaaaaaaaaa","receiver":"aa","text":"aq"}'}
        message = event['message']
        self.send(text_data=message)

# docker run -p 6379:6379 -d redis
# a = {'type': 'websocket', 'path': '/ws/chat/l/', 'raw_path': b'/ws/chat/l/', 'headers': [(b'host', b'127.0.0.1:8000'), (b'connection', b'Upgrade'), 
# (b'pragma', b'no-cache'), (b'cache-control', b'no-cache'), (b'user-agent', b'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
#  Chrome/108.0.0.0 Safari/537.36'), (b'upgrade', b'websocket'), (b'origin', b'http://127.0.0.1:8000'), (b'sec-websocket-version', b'13'), (b'accept-encoding', b'gzip, deflate, br'),
#  (b'accept-language', b'en-US,en;q=0.9,ar;q=0.8,fa;q=0.7,fr;q=0.6'), (b'cookie', b'csrftoken=dnIk0H5VCqgPjJ6NwQ9f3AUHZNSIUTspbefze3pKtLrsZ6LJ8wZbY6JKtk9GcUG0'), (b'sec-websocket-key', b'1F5W80A0K4RodUNroVdC3A=='), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits')], 'query_string': b'', 'client': ['127.0.0.1', 54225], 'server': ['127.0.0.1', 8000],
#      'subprotocols': [], 'asgi': {'version': '3.0'}, 'cookies': {'csrftoken': 'dnIk0H5VCqgPjJ6NwQ9f3AUHZNSIUTspbefze3pKtLrsZ6LJ8wZbY6JKtk9GcUG0'},
#  'session': < django.utils.functional.LazyObject object at 0x0000015E3A3E2910 > , 'user': < channels.auth.UserLazyObject object at 0x0000015E3A3E28B0 > ,
#  'path_remaining': '', 'url_route': {'args': (), 'kwargs': {'username': 'l'}}}
