import json
class TicketBooking():
    def __init__(self,passenger_name,passenger_age,passenger_nationality,passenger_passport_id,payment_method, ticketprice):
        self.passenger_name =  passenger_name
        self.passenger_age = passenger_age
        self.passenger_nationality = passenger_nationality
        self.passenger_passport_id = passenger_passport_id
        self.payment_method = payment_method
        self.ticketprice = ticketprice

    def bookingticket(self):

        if(self.payment_method == "CART"):
            print("Please enter card number")
            cardnumber = int(input())
            if(len(str(cardnumber)) == 16):
                print("Your payment method is succesfully registered")
            else:
                while True:
                    print("Please enter again card number")
                    cardnumber = int(input())
                    if (len(str(cardnumber)) > 16):
                        print("Your payment method is succesfully registered")
                        break
        else:
            print(f"Please give me {self.ticketprice} dollar")

