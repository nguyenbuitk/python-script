class Hotel:
    def __init__(self, name, rooms) -> None:
        self.name = name
        self.rooms = rooms
        self.booked_rooms = 0
    
    def book_room(self):
        if self.booked_rooms < self.rooms:
            self.booked_rooms += 1
            print(f"Room booked at {self.name}. Total booked rooms: {self.booked_rooms}")
        else:
            print(f"No rooms availabel at {self.name}")
    
    def available_rooms(self):
        return self.rooms - self.booked_rooms

# Creating instances of the Hotel class
hotel_1 = Hotel("Grand Hotel", 100)
hotel_2 = Hotel("Cozy Inn", 50)

# Booking rooms
hotel_1.book_room()
hotel_2.book_room()

# Checking available rooms
print(hotel_1.available_rooms())
print(hotel_2.available_rooms())