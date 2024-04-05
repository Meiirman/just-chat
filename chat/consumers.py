from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Получаем room_name из URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'{self.room_name}'
        
        # Присоединяемся к группе комнаты
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # Принимаем подключение
        await self.accept()

    async def disconnect(self, close_code):
        # Отключаемся от комнаты
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        # Получаем данные от WebSocket и отправляем их в комнату
        data = json.loads(text_data)
        message = data['message']
        nickname = data['nickname']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'nickname': nickname
            }
        )

    async def chat_message(self, event):
        # Отправляем сообщение обратно клиентам в комнате
        message = event['message']
        nickname = event['nickname']
        await self.send(text_data=json.dumps({
            'message': message,
            'nickname': nickname
        }))
