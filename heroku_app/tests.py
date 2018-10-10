from django.test import TestCase

# Create your tests here.


def double(x):
    return x * 2


class MyTest(TestCase):
    def test_double(self):
        self.assertEqual(double(2), 4)
