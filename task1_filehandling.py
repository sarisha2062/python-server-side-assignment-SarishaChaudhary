Students_names=[]
num = int(input("Enter the number of students to be  store in file : "))
for i in range(num):
    Name = input(f"Enter the name of the students: ")
    Students_names.append(Name)
    
#Store contents in the file
with open("Students.txt","w") as file:
    for Name in Students_names:
        file.write(Name + "\n")
        
#Read and display the contents
print("\nStudents Name :")
with open("Students.txt","r") as file:
    data = file.read()
    print(data)