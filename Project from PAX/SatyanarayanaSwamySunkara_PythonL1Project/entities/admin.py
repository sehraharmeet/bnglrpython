

class Admin:
    def approve(self, request, market):
        if request.req_type == "ADD":
            market.add_stock(request.stock, request.price)
        elif request.req_type == "REMOVE":
            market.remove_stock(request.stock)

        request.status = "APPROVED"

    def reject(self, request):
        request.status = "REJECTED"