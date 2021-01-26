#Envisioned and defined by Razvan Manescu

class Order:
    pick_up_address = (0, 0)
    drop_off_address = (0, 0)
    order_number = 0
    id = 0
    quantity = 1

    def __init__(self, id, order_number, pick_up_address, drop_off_address):
        self.pick_up_address = pick_up_address
        self.drop_off_address = drop_off_address
        self.order_number = order_number
        self.id = id

