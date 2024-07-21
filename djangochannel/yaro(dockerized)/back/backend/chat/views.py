from django.shortcuts import render
import json
from django.utils.safestring import mark_safe
def index(reqest):
    return render(reqest,'index.html')

def room(request,roomname):
    print(request.user)
    return render(request,'chatroom.html',{ 'roomname':mark_safe(json.dumps(roomname))})