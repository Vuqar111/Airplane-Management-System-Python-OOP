import  json
class AirplaneRestaurant:
    def __init__(self, foodname, foodprice, fooddetails):
        self.foodname = foodname
        self.foodprice = foodprice
        self.fooddetails = fooddetails

    def givedetails(self):
        pass

    def bookingfood(self, foodname):
            try:
                with open('foods.json', 'r') as f:
                    foods = json.load(f)
                    for food in foods:
                        if food['foodname'] == foodname:
                            return food
            except:
                return "There is no food this name"
    

    def search(self,db_name, foodname):
            try:
                with open(db_name, 'r') as f:
                    users = json.load(f)
                    for user in users:
                        if user['foodname'] == foodname:
                            return food
            except:
                return "There find Food"   


    def bookingticket(self):
        pymethod = input("Please enter cart name CASH--1 CART--2")
        if(pymethod == 2):
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
                print(f"Please give me {self.foodprice}  dollar")