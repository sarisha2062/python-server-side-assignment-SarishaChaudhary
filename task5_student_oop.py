class Students :
    def __init__ (self):
        self.name = ""
        self.roll_no = ""
        self.marks = ""
        
    def  details(self):
        self.name = input("Enter name of student : ")
        self.roll_no = int(input("Enter roll number of student : "))
        total_subject = int(input("Enter number of subject : "))
        self.marks =[] 
        for i in range (total_subject):
            mark = int(input(f"Enter the marks subject {i + 1 } : "))
            self.marks.append(mark)
            
    def display(self):
        print("Students Details")
        print(f"Name : {self.name}")
        print(f"Roll Number : {self.roll_no}")
        print(f"Marks : {self.marks}")
        
Student1 = Students()
Student1.details()
Student1 .display()