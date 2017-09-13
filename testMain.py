import unittest
import main
import json

class TestMain(unittest.TestCase):

    def test_cartprice(self):
        cart = json.loads('{\
            "product-type": "hoodie",\
            "options": {\
            "size": "small",\
            "colour": "dark",\
            "print-location": "front"\
            },\
            "artist-markup": 20,\
            "quantity": 2\
            }')
        data_price = json.loads('[\
  {\
    "product-type": "hoodie",\
    "options": {\
      "colour": ["white", "dark"],\
      "size": ["small", "medium"]\
    },\
    "base-price": 3800\
  },\
  {\
    "product-type": "hoodie",\
    "options": {\
      "size": ["large"],\
      "colour": ["white"]\
    },\
    "base-price": 3848\
  },\
  {\
    "product-type": "hoodie",\
    "options": {\
      "colour": ["white"],\
      "size": ["xl", "2xl", "3xl"]\
    },\
    "base-price": 4108\
  }\
  ]')
        self.assertEqual(main.calculateItemPrice(cart, data_price), 9120)

if __name__ == '__main__':
    unittest.main()