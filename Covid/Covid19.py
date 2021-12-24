class Covid19:
    def __init__(self,age):
        self.age = age


    def  checkcovid(self):
        try:
          if(self.age > 18):
              covidname = input("PLease enter covid name")
              if(covidname):
                  print("You can enter inside airport")
          else:
              print("You can enter inside airport")
        except:
             print("Something went wrong")



