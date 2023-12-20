import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceBIsZero(self):
    price_a = 123.45
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))

  def test_getRatio_priceAIsZero(self):
    price_a = 0 
    price_b = 123.45
    self.assertEqual(getRatio(price_a, price_b), 0)

  def test_getRatio_equalPrices(self):
    price_a = 100.0
    price_b = 100.0
    self.assertEqual(getRatio(price_a, price_b), 1.0)
  
  def test_getDataPoint_invalidData(self):
      quote = {'top_ask': {'price': None, 'size': None}, 'top_bid': {'price': None, 'size': None}, 'stock': 'GHI'}
      with self.assertRaises(TypeError):
          getDataPoint(quote)


if __name__ == '__main__':
    unittest.main()
