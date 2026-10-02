student = {}

while True:
  print("n/----STUDENT MANAGEMENT SYSTEM----")
  print("1. Add Student")
  print("2. View Students")
  print("3. Check Result)
print("4. Add Exit")

        choice = input("Enter your choice:")

#Add Student
if choice == "1":
    name = input("Enter student name:")
    marks = int(input("Enter marks:"))
    student[name] = marks
    print(f"{name} Sucessfully Added!")
      
#view students
elif choice == "2":
  if not students:
    print("No student found!")
else:
  for name, marks in student.items():
      print(name, ":",marks)

#check result
elif choice =="3":
    name = input("Enter student name:")

if name in student:
    marks = student[name]

    if marks >= 40:
        print("PASS")
    else:
        print("FAIL")

else:
    print("Student Not Found!")

#exit
elif choice == "4":
     print("Exiting....")
     break

else:
    print("In-valid input")

   

  
