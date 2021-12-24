import json
from RecordFlight.CenterFlights import CenterFlight
class Fuzuli(CenterFlight):
    def __init__(self, flightid, flightname,location,destination, startingtime, typeflight, reachingtime,price, capacity):
        super().__init__(flightid, flightname,location,destination, price, typeflight)
        self.capacity = capacity
        self.startingtime = startingtime
        self.reachingtime = reachingtime
        self.price = price



    def serialize(self):
        return {
            'flightid': self.flightid,
            'flightname': self.flightname,
            'capacity': self.capacity,
            'startingtime': self.startingtime,
            'reachingtime': self.reachingtime,
            'source': self.source,
            'destination': self.destination,
            'price': self.price,
            'type': self.typeflight
        }


    def to_json(self, file):
        try:
            with open(file, 'r+') as f:
                flights = json.load(f)
                for user in flights:
                    if user['flightid'] == self.flightid:
                        return "User already exists(deqiq olsun)"
                f.seek(0)
                flights.append(self.serialize())
                json.dump(flights, f)
            return "Flight added"
        except:
            with open(file, 'w') as f:
                json.dump([self.serialize()], f)
            return "User added"





class SearchFuzuliAirplane():
        def search(self,db_name, flightid):
            try:
                with open(db_name, 'r') as f:
                    users = json.load(f)
                    for user in users:
                        if user['flightid'] == flightid:
                            return user
            except:
                return "There is no Flight"


class RemoveFuzuliAirplane():
    def removeflight(self, db_name,  flightid):
        try:
            with open(db_name, 'r+') as f:
                users = json.load(f)
                for user in users:
                    if user['flightid'] == flightid:
                        users.remove(user)
                        f.seek(0)
                        f.truncate()
                        json.dump(users, f, indent=4)
                        return "Successfully removed flight"
                return "Flight not found"
        except:
            return "There is no Flight Id"



