print("Welcome to our Airport \n Let's check that our airport working or not at this time")
from AirportManagement.AirportManagement import AirportManagement
airport = AirportManagement("BakuAirport",input("Please enter date"))
airport.open()

print("Okay please enter vaccine")
from Covid.Covid19 import Covid19
Covid19 = Covid19(int(input("Please enter age")))
Covid19.checkcovid()


from Authentication import regist
Register = regist.Register()
print("Please enter information's for register")
Register.register(input("Please enter name"), input("Please enter password"),input("Please enter email"),input("Please enter phone number"))
Register.login(input("Please enter username"), input("Please enter password"))


from HaydarAliyev.HaydarAliyev import  HaydarAliyev
from HaydarAliyev.HaydarAliyev import  SearchHaydarAliyev
from HaydarAliyev.HaydarAliyev import RemoveHaydarAliyev
from Lenkeran.Lenkeran import  Lenkeran
from Lenkeran.Lenkeran import  SearchLenkeranAirplane
from Lenkeran.Lenkeran import  RemoveLenkeranAirplane
from Fuzuli.Fuzuli import  Fuzuli
from Fuzuli.Fuzuli import  SearchFuzuliAirplane
from Fuzuli.Fuzuli import  RemoveFuzuliAirplane
from Nakchivan.Nakcivan import  Nakchivan
from Nakchivan.Nakcivan import SearchNaAirplane
from Nakchivan.Nakcivan import RemoveNakchivanAirplane
from TicketBooking.TicketBooking import  TicketBooking
from Employers.AirplaneEmployees import AirplaneEmployees
from Employers.AirportEmployees import AirportEmployees
from LuggagePayment.Luggage import  Luggage
from AirplaneRestaurant.AirplaneRestaurant import  AirplaneRestaurant




print("Are you Customer or Employeer \n 1-Employer \n 2- Customer")
role = int(input("Please choose your role"))
if(role == 1):
   print("Do you want to work with employee or flight")
   print("Employee -- 1 \n Flight -- 2 ")
   answer = int(input("please enter answer"))
   if(answer == 1):
       print("Which area do you want to initialize")
       key = int(input("Pls enter 1-Airport 2-Airplane"))
       if(key == 1):
            print("Please enter action enter key 1-add, 2-remove, 3-print")
            action = int(input("PLease enter action"))
            if (action == 1):
                dev = AirportEmployees("Lady", "Ladia", 3000, "Pilot", "Airplane", [])
                print(dev.add_emp(input("PLease enter name")))
            elif (action == 2):
                dev = AirportEmployees("Lady", "Ladia", 3000, "Pilot", "Airplane", [])
                print(dev.remove_emp(input("PLease enter name")))
            elif (action == 3):
                dev = AirportEmployees("Lady", "Ladia", 3000, "Pilot", "Airplane", [])
                print(dev.print_emps())
            else:
                print("There is no other action in here")
       elif(key == 1):
           print("Please enter action enter key 1-add, 2-remove, 3-print")
           action = int(input("PLease enter action"))
           if (action == 1):
               dev = AirplaneEmployees("Lady", "Ladia", 3000, "Pilot", "Airplane", [])
               print(dev.add_emp(input("PLease enter name")))
           elif (action == 2):
               dev = AirplaneEmployees("Lady", "Ladia", 3000, "Pilot", "Airplane", [])
               print(dev.remove_emp(input("PLease enter name")))
           elif (action == 3):
               dev = AirplaneEmployees("Lady", "Ladia", 3000, "Pilot", "Airplane", [])
               print(dev.print_emps())
           else:
               print("There is no other action in here")


   elif(answer == 2):
       print("We have 4 airport areas, Please choose on of them \n Haydar Aliyev --1 \n Lenkeran -- 2 \n Fuzuli -- 3 \n Nakchivan -- 4")
       key = int(input("Please enter number 1,2,3,4"))
       if(key == 1):
           print("Which action do you want to make \n ADD-1, Search - 2, Remove - 3")
           action1 = int(input("Please enter key"))
           if(action1 == 1):
               flightadded = HaydarAliyev(input("Please enter flight id"),input("Please enter flight name"),input("Please enter flight location"),input("Please enter flight destionation"),input("Please enter flight startingtime"),input("Please enter type of flight"),input("Please enter reaching time"),input("Please enter flight price"),input("Please enter flight capacity"))
               print(flightadded.to_json('haydaraliyev.json'))
           elif(action1 == 2):
               searchHaydarAliyev = SearchHaydarAliyev()
               print(searchHaydarAliyev.search('haydaraliyev.json', input("Enter Flight Id")))
           elif(action1 == 3):
               removelenkeranairplane = RemoveHaydarAliyev()
               print(removelenkeranairplane.removeflight('haydaraliyev.json', input('Enter FlightId:')))
           else:
               print("You have no action")
       elif(key == 2):
           print("Which action do you want to make \n ADD-1, Search - 2, Remove - 3 in Lenkeran Airplane")
           action2 = int(input("Please enter key"))
           if (action2 == 1):
               flightadded = Lenkeran(input("Please enter flight id"),input("Please enter flight name"),input("Please enter flight location"),input("Please enter flight destionation"),input("Please enter flight startingtime"),input("Please enter type of flight"),input("Please enter reaching time"),input("Please enter flight price"),input("Please enter flight capacity"))
               print(flightadded.to_json("lenlenkeranairplane.json"))
           elif (action2 == 2):
               searchlenkeranairplane = SearchLenkeranAirplane()
               print(searchlenkeranairplane.search('lenkeranairplane.json', input("Enter Flight Id")))
           elif (action2 == 3):
               removelenkeranairplane = RemoveLenkeranAirplane()
               print(removelenkeranairplane.removeflight('lenkeranairplane.json', input('Enter FlightId:')))
           else:
               print("You have no other action")
       elif (key == 3):
           print("Which action do you want to make \n ADD-1, Search - 2, Remove - 3 in Fuzuli Airplane")
           action3 = int(input("Please enter key"))
           if (action3 == 1):
               flightadded = Fuzuli(input("Please enter flight id"),input("Please enter flight name"),input("Please enter flight location"),input("Please enter flight destionation"),input("Please enter flight startingtime"),input("Please enter type of flight"),input("Please enter reaching time"),input("Please enter flight price"),input("Please enter flight capacity"))
               print(flightadded.to_json("fuzuli.json"))
           elif (action3 == 2):
               searchfuzuliairplane = SearchFuzuliAirplane()
               print(searchfuzuliairplane.search("fuzuli.json", input("Enter flight id")))
           elif (action3 == 3):
               removefuzuliairplane = RemoveFuzuliAirplane()
               print(removefuzuliairplane.removeflight('fuzuli.json', input('Enter FlightId:')))
           else:
               print("You have no other action")
       elif (key == 4):
           print("Which action do you want to make \n ADD-1, Search - 2, Remove - 3 in Nakchivan Airplane")
           action4 = int(input("Please enter key"))
           if (action4 == 1):
               flightadded = Nakchivan(input("Please enter flight id"),input("Please enter flight name"),input("Please enter flight location"),input("Please enter flight destionation"),input("Please enter flight startingtime"),input("Please enter type of flight"),input("Please enter reaching time"),input("Please enter flight price"),input("Please enter flight capacity"))
               print(flightadded.to_json("nakchivan.json"))
           elif (action4 == 2):
               searchnakchivan = SearchNaAirplane()
               print(searchnakchivan.search("nakchivan.json"), input("Enter Flight Id"))
           elif (action4 == 3):
               removenakchivan = RemoveNakchivanAirplane()
               print(removenakchivan.removeflight('nakchivan.json', input('Enter FlightId:')))

           else:
               print("You have no other action")

elif(role == 2):
    print("Which airlane area do you want to search")
    print("We have 4 airport areas, Please choose on of them \n Haydar Aliyev --1 \n Lenkeran -- 2 \n Fuzuli -- 3 \n Nakchivan -- 4")
    ans = int(input("pls enter ans"))
    if(ans == 1):
        searchHaydarAliyev = SearchHaydarAliyev()
        print(searchHaydarAliyev.search('haydaraliyev.json', input("Enter Flight Id")))
    elif(ans == 2):
        searchlenkeranairplane = SearchLenkeranAirplane()
        print(searchlenkeranairplane.search("lenkeranairplane.json", input("Enter Flight Id")))
    elif(ans == 3):
        searchfuzuliairplane = SearchFuzuliAirplane()
        print(searchfuzuliairplane.search("fuzuli.json", input("Enter Flight Id")))
    elif(ans == 4):
        searchnakchivanairplane = SearchNaAirplane()
        print(searchnakchivanairplane.search("nakchivan.json", input("Enter Flight Id")))
    answerkey = input("Do you want to ticket YES OR NOT")
    if(answerkey == "YES"):
        ticket = TicketBooking(input("Please enter name"), input("Passenger Age"), input("Passenger Nationality"),
                               input("PassengerId"), input("Passenger Method"), 500)
        ticket.bookingticket()
    else:
        print()
    print("Do you have luggage")
    ans = input("Please enter answer YES OR NOT: ")
    if(ans == "YES"):
        obj = Luggage(input("PLease enter id: "),input("Please enter passenger id: "), input("Please enter flight id"), int(input("PLease enter number of lunguage")))
        obj.bookingticket()
    else:
        print("Something went wrong") 
    print("Do you eat something between waiting time's")
    eataction = input("Please enter YES or NOT: \n 1-YES \n 2- NOT ")
    if(eataction == "YES"):
        obj = AirplaneRestaurant("Dolma", 24, "It is random details")
        print(obj.search("foods.json", input("Enter food name")))
        answer =  int(input("Do you want to buy this name? 1--YES, 2--NO")) 
        if(answer == 1):
            obj = AirplaneRestaurant("Dolma", 24, "It is random details")
            print(obj.bookingticket())  
        else:
            print("So we can not give you food bro")
    else:
        print("Okay, Goodbye")



