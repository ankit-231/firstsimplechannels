import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    # when frontend makes a connection to the websocket, this is run
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept
        self.accept()

    # when frontend sends any message to websocket, this is run
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        lol = text_data_json['message']

        print(lol)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': lol + ' lmao'
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message + ' ???why '
        }))

