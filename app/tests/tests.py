from django.test import TestCase
import pytest 



class Tests(TestCase):

    def test_add():
        a = 10
        b = 10

        assert a + b == 10
