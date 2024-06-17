import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)

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

class CreditCard:
    def __init__(self, number):
        self.number = number
    
    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number,
                     "expiration":  expiration,
                     "holder": holder,
                     "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

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
        
        