class Luggage:
    def __init__(self,luggageid, passengerid,flightid,noOfluggages):
        self.luggageid = luggageid
        self.passengerid = passengerid
        self.flightid = flightid
        self.noOflugagges = noOfluggages

    def bookingticket(self):
        if(self.noOflugagges > 5):
            print("Your cargo price is 100$ \n Do you want to continue")
            answer = input("If you want to continue please enter paymnent method")
            if(answer == "CART"):
                    print("Please enter card number")
                    cardnumber = int(input())
                    if (len(str(cardnumber)) == 16):
                        print("Your payment method is succesfully registered")
                    else:
                        while True:
                            print("Please enter again card number")
                            cardnumber = int(input())
                            if (len(str(cardnumber)) > 16):
                                print("Your payment method is succesfully registered")
                                break
                            else:
                                print(f"Please give me {self.noOflugagges * 10} dollar")

        elif(self.noOflugagges < 5):
            print("Your cargo price is 10$")
            print("Your cargo price is 100$ \n Do you want to continue")
            answer = input("If you want to continue please enter paymnent method")
            if (answer == "CART"):
                print("Please enter card number")
                cardnumber = int(input())
                if (len(str(cardnumber)) == 16):
                    print("Your payment method is succesfully registered")
                else:
                    while True:
                        print("Please enter again card number")
                        cardnumber = int(input())
                        if (len(str(cardnumber)) > 16):
                            print("Your payment method is succesfully registered")
                            break
                        else:
                            print(f"Please give me {self.noOflugagges * 10} dollar")
        else:
            print("Your cargo price is 1000$")
            print("Your cargo price is 100$ \n Do you want to continue")
            answer = input("If you want to continue please enter paymnent method")
            if (answer == "CART"):
                print("Please enter card number")
                cardnumber = int(input())
                if (len(str(cardnumber)) == 16):
                    print("Your payment method is succesfully registered")
                else:
                    while True:
                        print("Please enter again card number")
                        cardnumber = int(input())
                        if (len(str(cardnumber)) > 16):
                            print("Your payment method is succesfully registered")
                            break
                        else:
                            print(f"Please give me {self.noOflugagges * 10} dollar")


