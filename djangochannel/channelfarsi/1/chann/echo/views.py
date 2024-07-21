from django.shortcuts import render,HttpResponse
from django.utils.safestring import mark_safe
import json
# Create your views here.
def index(request):
    return render(request, 'echo/index.html')
        # return render(request, 'echo/index.html',context={'text':'aaaaaaaaa'})
def echo_image(request):
    return render(request, 'echo/echo_image.html')

def joinchat(request, username):
    return render(request, 'echo/join_chat.html', {'username_json': mark_safe(json.dumps(username))})

# http://localhost:8000/chat/new/sender/?receiver=b&text=hello
# ba balai yekie http://localhost:8000/chat/new/sender?receiver=b&text=hello
# bayad safeye chat ro morajee kone va esmiro ke bahash login kardi ro too receiver benevisi
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
def newmessage(request, username):
    receiver = request.GET['receiver']
    text = request.GET['text']
    channel_layer = get_channel_layer()
    group_name = f"chat_{receiver}"

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'chat_message',
            'message': json.dumps({'sender': username, 'receiver': receiver, 'text': text})
        }
    )

    return HttpResponse('Message Sent')