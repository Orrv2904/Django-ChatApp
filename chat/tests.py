from django.test import TestCase
from datetime import datetime
from .models import Room, Message

class RoomModelTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(name="Test Room")

    def test_room_name(self):
        self.assertEqual(self.room.name, "Test Room")

class MessageModelTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(name="Test Room")
        self.message = Message.objects.create(
            value="Test Message",
            date=datetime.now(),
            user="Test User",
            room=self.room
        )

    def test_message_value(self):
        self.assertEqual(self.message.value, "Test Message")

    def test_message_date(self):
        self.assertIsInstance(self.message.date, datetime)

    def test_message_user(self):
        self.assertEqual(self.message.user, "Test User")

    def test_message_room(self):
        self.assertEqual(self.message.room, self.room)
