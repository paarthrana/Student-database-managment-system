student={
    "name": "John Doe",
    "Roll no": "101",
    "percentage": 89
    } 

students =[]
students.append(student)

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter student roll number: ")
    percentage = float(input("Enter student percentage: "))

    student ={
        "name": name,
        "Roll no": roll_no,
        "percentage": percentage
    }
    students.append(student)
    
def display_student():
   if len(students)==0:
            print("No students in the database.")
   else:
            for student in students:
                print(student)


topper = max(students, key=lambda x: x['percentage'])

while True:
    print("\n-------Student Database Management System-------")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    print("4. Display Topper")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':       
        display_student()

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    elif choice == '4':
        print("Topper of the class is:", topper['name'], "with percentage:", topper['percentage'])  
    else:        print("Invalid choice....")