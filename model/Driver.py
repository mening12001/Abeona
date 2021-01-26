#Envisioned and defined by Razvan Manescu

class Driver:
    capacity = 0
    id = 0
    first_name = 0
    last_name = 0
    current_location = "0,0"

    def __init__(self, id, first_name, last_name, current_location, capacity):
        self.capacity = capacity
        self.first_name = first_name
        self.last_name = last_name
        self.current_location = current_location
        self.capacity = capacity
        self.id = id