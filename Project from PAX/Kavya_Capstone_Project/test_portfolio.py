import unittest

class TestPortfolioCalculations(unittest.TestCase):

    def test_profit_calculation(self):
        buy_price = 100
        current_price = 150
        quantity = 10

        profit = (current_price - buy_price) * quantity
        self.assertEqual(profit, 500)

    def test_loss_calculation(self):
        buy_price = 200
        current_price = 150
        quantity = 5

        loss = (buy_price - current_price) * quantity
        self.assertEqual(loss, 250)

    def test_no_profit_no_loss(self):
        buy_price = 100
        current_price = 100
        quantity = 20

        result = (current_price - buy_price) * quantity
        self.assertEqual(result, 0)

    def test_average_price_calculation(self):
        old_qty = 10
        old_price = 100
        new_qty = 10
        new_price = 200

        total_cost = (old_qty * old_price) + (new_qty * new_price)
        avg_price = total_cost / (old_qty + new_qty)

        self.assertEqual(avg_price, 150)


if __name__ == "__main__":
    unittest.main()
