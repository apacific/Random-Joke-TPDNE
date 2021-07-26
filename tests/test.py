import unittest
import requests
from unittest.mock import Mock
from main import home

requests = Mock()

class test(unittest.TestCase):
    data = requests.get('https://v2.jokeapi.dev/joke/Programming')
    
    def test_home_page(self):
        self.assertEqual(1+1, 2)
        print(dir(requests))  # This shows us available methods to use with an object.
        print(requests.get.assert_called())
#        print(requests.get.assert_not_called())
        print(requests.get.assert_called_with('https://v2.jokeapi.dev/joke/Programming'))
        print(requests.method_calls)


if __name__ == '__main__':
    unittest.main()
