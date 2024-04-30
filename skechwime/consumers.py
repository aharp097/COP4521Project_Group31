from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CanvasConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['lobby_name']
        self.room_group_name = f'canvas_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            data_json = json.loads(text_data)
            print("Received data:", data_json)
            action = data_json['action']
            x = data_json['x']
            y = data_json['y']
            color = data_json['color']
        except json.JSONDecodeError as e:
            print("Error decoding JSON", str(e))
        # Send the received action to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'canvas_action',
                'action': action,
                'x': x,
                'y': y,
                'color': color
            }
        )

    async def canvas_action(self, event):
        print("Broadcasting to group:", event)
        await self.send(text_data=json.dumps({
            'action': event['action'],
            'x': event['x'],
            'y': event['y'],
            'color': event['color']
        }))
