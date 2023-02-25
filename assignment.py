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
        self.age = int(input("Enter the age of user"))


    def show_user(self):
        return self.name, self.email, self.address, self.age

# Train dictionary with train details and fare
train_data ={1:{'From':'Pune', 'To':'Latur', 'train_no':12345, 'Fare':{'first_class':1250, 'second_class':800, 'third_class':600, 'sleeper_class':250, 'seating_class':100}}, 2:{'From':'Latur', 'To':'Pune', 'Train_no':54321, 'Fare':{'first_class':1250, 'second_class':800, 'third_class':600, 'sleeper_class':250, 'seating_class':100}}}



#Ticket class for ticket management
class Ticket:
    '''def __init__(self, id, date):
        self.id = id
        self.date = date'''
    # Getting user details from user class
    user()
    User = user.show_user()   
    
    # create Book ticket method for ticket booking 
    def book_ticket(self, train_data):
        print(f"Follwing is the data of trains currently ongoing")
        
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

        # Use of short hand if statement 
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
        




if __name__ == "__main__":
    a = Ticket()
    a.book_ticket(train_data)