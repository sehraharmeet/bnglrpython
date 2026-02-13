import unittest
from models import User

class TestPortfolio(unittest.TestCase):

    def test_buy_stock(self):
        user = User("test", "123")
        user.buy_stock("AAPL", 2, 100)
        self.assertEqual(user.portfolio["AAPL"], 2)

    def test_sell_stock(self):
        user = User("test", "123")
        user.buy_stock("AAPL", 2, 100)
        user.sell_stock("AAPL", 1, 100)
        self.assertEqual(user.portfolio["AAPL"], 1)


if __name__ == "__main__":
    unittest.main()