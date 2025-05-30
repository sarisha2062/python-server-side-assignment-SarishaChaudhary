Students={}
def Add():
    Roll = int(input("Enter Roll Number: "))
    if Roll in Students:
        print("This roll number already exists")
        return
    Name = input("Enter the name: ")
    Marks = input("Enter the marks: ")
    Contact_Number = input("Enter the contact number: ")
    Students[Roll]={
        "Name": Name,
        "Marks": Marks,
        "Contact Number": Contact_Number
    }
    print("Added Successfully!\n")

def Search():
    Roll = int(input("Enter Roll Number: "))
    if Roll in Students:
        print("Record Found: ")
        for key , value in Students[Roll].items():
            print (f"{key} : {value}")
    else:
        print("Doesn't Exist!\n")

def Display():
    if not Students:
        print("No record exist")
    else:
        for roll , detail in Students.items():
            print(f"Roll Number : {roll}")
            for key , value in detail.items():
                print (f"{key} : {value}")
                
while True:
    print("Students Record Menu ")
    print("1. Add")
    print("2. Search")
    print("3. Display")
    print("4. Exit")
    
    choice = input("Enter your choice (1 to 4) : ")
    if choice == '1':
        Add()
    elif choice == '2':
        Search()
    elif choice == '3':
        Display()
    elif choice == '4':
        print(" Exiting....")
        break
    else:
        print("Invalid Choice. Please choose number between 1 to 4.")