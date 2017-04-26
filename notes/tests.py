from django.test import TestCase
from accounts.models import User
from .models import *
import datetime


# Create your tests here.
class NoteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test')
        self.tag1 = Tag.objects.create(name='tag1')
        self.tag2 = Tag.objects.create(name='tag2')
        self.note1 = Note.objects.create(
            title='test title',
            content='本日は晴天なり',
            locate='location',
            date=datetime.date.today(),
            start_time=datetime.datetime.now(),
            end_time=datetime.datetime.now(),
            elapsed_time=10,
            user=self.user,
            text_type=1
        )
        self.note1.tag.add(self.tag1)
        self.note1.tag.add(self.tag2)

    def tearDown(self):
        user = User.objects.get(username='test')
        user.delete()
        self.tag1.delete()
        self.tag2.delete()

    def test_normal(self):
        notes = Note.objects.all()
        self.assertTrue(self.note1 in notes)

    def test_tag_list(self):
        self.assertEqual(self.note1.tag_list(), 'tag1, tag2')
