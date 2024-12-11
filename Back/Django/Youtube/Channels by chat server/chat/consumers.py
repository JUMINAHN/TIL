# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer
#websocket 자체를 불러오고 -> websocket의 consumer을 불러야 함

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))