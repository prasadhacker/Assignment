# import statement
import random 
import string


# user class for user details and get user info
class user:
    def __init__(self):
        self.name = ''
        self.email = ''
        self.address = ''
        self.age = 0
    
    def get_user_info(self):
        print("Enter user details:")
        self.name = input("Enter the Name of user:")
        self.email = input("Enter the email of user:")
        self.address = input ("Enter the Address of user:")
        self.age = int(input("Enter the age of user:"))

    def show_user(self):
        return self.name, self.email, self.address, self.age

# Train dictionary with train details and fare
train_data ={1:{'From':'Pune', 'To':'Latur', 'train_no':12345, 'Fare':{'first_class':1250, 'second_class':800, 'third_class':600, 'sleeper_class':250, 'seating_class':100}}, 2:{'From':'Latur', 'To':'Pune', 'train_no':54321, 'Fare':{'first_class':1250, 'second_class':800, 'third_class':600, 'sleeper_class':250, 'seating_class':100}}}


#Ticket class for ticket management
class Ticket:
    # Getting user details from user class

    # create Book ticket method for ticket booking 
    def book_ticket(train_data):
        print(f"Following is the data of trains currently ongoing")
        
        # For loop To Print All Train Details in Dictionary
        for train in train_data:
            Train=train_data[train]
            Fare=Train.get('Fare')
            print(f"{train}: Train Number: {Train.get('train_no')}\n   Start From : {Train.get('From')}\n   Stop At:{Train.get('To')}\n   Fare:1=First Class:{Fare.get('first_class')}\n        2=Second Class:{Fare.get('second_class')}\n        3=Third Class:{Fare.get('third_class')}\n        4=Sleeper Class:{Fare.get('sleeper_class')}\n        5=Seating Class:{Fare.get('seating_class')}")
        
        # Getting Choices of train and fair
        print("Select the choice of train you Want")
        train_choice = int(input())
        print("Select the choice of Fare you Want")
        fare_choice = int(input())
        
        # Getting Train Details
        Train=train_data.get(train_choice)

        # Use of if statement seat preference 
        if fare_choice==1 :
            fare_choice = "first_class"
        elif fare_choice==2 :
            fare_choice = "second_class" 
        elif fare_choice==3 :
            fare_choice = "third_class" 
        elif fare_choice==4 :
            fare_choice = "sleeper_class" 
        else:
            fare_choice = "seating_class"
        
        # Getting Fare Value
        fare = Train.get('Fare')
        Fare = fare.get(fare_choice)
        
        #Function to create PNR (Random String)
        def get_random_string(length):
            letters = string.ascii_uppercase
            result_str = ''.join(random.choice(letters) for i in range(length))
            return result_str
        PNR = get_random_string(5)
        
        #Function to create ticket number()
        def create_ticket_number(length):
            digits = string.digits
            result_str = ''.join(random.choice(digits) for i in range(length))
            return result_str
        ticket_number = create_ticket_number(8)
        return PNR, ticket_number, Fare, fare_choice, Train


def main():
    print (f"Welcome to the Train Ticket Booking")
    passenger_number= int(input('Enter the number of passenger:'))
    U = {}
    for i in range(passenger_number):
        a = user()
        User = a.get_user_info()
        U["User{0}".format(i)]=a.show_user()

    T=Ticket.book_ticket(train_data)
    PNR = T[0]
    ticket_number = T[1]
    Fare = T[2]
    Seat_preference = T[3]
    Train = T[4]
    Total_Fare = Fare*passenger_number
    
    #calculation of Discounted fare 
    discounted_fare = 0
    j=0
    for i in U:
        age=U[i][3]
        if age > 0 and age <= 2:
            fare=Fare/4
        elif age > 2 and age <= 60:
            fare = Fare
        else:
            fare = Fare/2
        discounted_fare +=fare
        j+=1
    discount = Total_Fare-discounted_fare
    print("PNR:",PNR)
    print("Ticket Number",ticket_number)
    print(f"Train Number: {Train.get('train_no')}\nStart From : {Train.get('From')}\nStop At:{Train.get('To')}")
    print("Seat Preference :",Seat_preference)
    print("Fare:",Total_Fare)
    print("Discount:",discount)
    print("Total Fare:",discounted_fare)
    for i in U:
        print("Passenger's Name:",U[i][0])
        print("Passenger's Email:",U[i][1])
        print("Passenger's address:",U[i][2])
        print("Passenger's age:",U[i][3])


if __name__ == "__main__":
    main()