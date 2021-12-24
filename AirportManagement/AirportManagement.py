from datetime import datetime
class AirportManagement:
    def __init__(self,cityname,time):
        self.cityname = cityname
        self.time = time

    def open(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if(current_time < "18:00"):
            print("Airport is open")
        else:
            print("Airport is not open")
    def display_airport_details(self):
        return f"Airport's located city name:{self.cityname}  \n"


