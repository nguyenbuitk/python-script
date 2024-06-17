import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        # return name of hotel with specific ID
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        
    def book(self):
        """Book a hotel by changing its availability to no"""
        
        # return availability of hotel
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # index=False: Excludes the row indices from the CSV file.
        df.to_csv("hotels.csv", index=False)
    
    def available(self):
        """Check if the hotel is available"""
        return df.loc[df["id"] == self.hotel_id, "available"].squeeze() == "yes"
    

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    
    def generate(self):
        content = f"""
        Thank you for your reserveraion!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id=hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name,hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")
        
        