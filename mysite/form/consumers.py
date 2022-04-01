from channels.generic.websocket import AsyncWebsocketConsumer
import json
import os
from datetime import datetime, timedelta



class ChatConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        self.room_group_name = 'task_layer'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.isalive()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        def myconverter(o):
            if isinstance(o, datetime):
                return o.__str__()

            # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }, default=myconverter))


    async def isalive(self):
        time_2 = datetime.now()
        await self.chat_message({'message': time_2})
        time_debug = os.path.getmtime(r"C:\Users\cjulemont\PycharmProjects\Django_project\elasticsearch_2\output\Hoja1_validate.xlsx")
        max_time_str = datetime.fromtimestamp(time_debug)

        if (datetime.now() - timedelta(minutes=1)).ctime()  < max_time_str.ctime():
            time_2 = datetime.now()
            await self.chat_message({'message': 'Please load your file and refresh the page'})

            # delta = time_2 - timedelta(minutes=80)
            # await self.chat_message({'message': str('your file has been processed with success, please follow the link below and dowmload your file')})


        else :
            await self.chat_message({'message': 'Please load your file and refresh the page'})




