from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'chat/main.html')

def chat(request, room_name, nickname):
    return render(request, 'chat/chat.html', {
        'room_name': room_name,
        'nickname': nickname
    })