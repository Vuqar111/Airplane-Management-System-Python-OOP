class Register:

    def __init__(self, username=None, password=None, email=None, phone_number=None) -> object:
        self.__username = username
        self.password = password
        self.email = email
        self.phone_number = phone_number


    def get_username(self):
        return self.__username

    def get_password(self):
        return self.password 

    def get_email(self):
        return self.email

    def get_phonenumber(self):
        return self.phone_number
    

    def set_username(self, username):
        self.__username = username

    def set_username(self, password):
        self.password = password

    def set_username(self, email):
        self.email = email    
     
    def set_username(self, phone_number):
        self.phone_number = phone_number 

   

    def login(self, entered_username, entered_password):
        if entered_username == self.__username and entered_password == self.password:
            print("Logged in successfully for : \n", self.__username)
        else:
            print("Username or password is incorrect")

    def register(self, username, password, email, phone_number):
        if username and password and email and phone_number:
            print("Registration successful for user : \n", username)
            self.__username = username
            self.password = password
            self.email = email
            self.phone_number = phone_number
        else:
            print("Unsuccessful")

