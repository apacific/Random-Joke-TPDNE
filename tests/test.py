import unittest
import requests
from main import home

class test(unittest.TestCase):
    data = requests.get("https://v2.jokeapi.dev/joke"
                        "/Programming").json().items()
    
    def test_home_page(self):
        assertEqual(1+1, 2)


if __name__ == '__main__':
    unittest.main()
