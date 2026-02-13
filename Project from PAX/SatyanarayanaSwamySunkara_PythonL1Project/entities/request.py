

class StockRequest:
    def init(self, req_id, req_type, stock, price=None, status="PENDING"):
        self.req_id = req_id
        self.req_type = req_type
        self.stock = stock
        self.price = price
        self.status = status