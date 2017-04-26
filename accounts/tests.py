from django.test import TestCase
from .models import *


# Grade test
class GradeTest(TestCase):
    def setUp(self):
        self.grade1 = Grade.objects.create(name='grade1', formal_name='Grade 1', priority=100)
        self.grade2 = Grade.objects.create(name='grade2', formal_name='Grade 2', priority=10)

    def test_normal(self):
        before = Grade.objects.all()
        self.assertTrue(self.grade1 in before)
        self.assertTrue(self.grade2 in before)

    def test_delete(self):
        self.grade1.delete()
        after = Grade.objects.all()
        self.assertTrue(self.grade1 not in after)


# User test
class UserTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username='hello',
            first_name='first',
            last_name='last'
        )

    def test_normal(self):
        users = User.objects.all()
        self.assertTrue(self.user1 in users)


class BelongTest(TestCase):
    pass
