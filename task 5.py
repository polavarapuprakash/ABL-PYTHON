students = []
attendance = []
marks = []
events = []
resources = ("Books", "Projectors", "Computers")

while True:
    print("\n--- SMART CAMPUS MANAGEMENT ---")
    print("1. Add Student")
    print("2. Record Attendance")
    print("3. Enter Marks")
    print("4. Register for Event")
    print("5. Allocate Resource")
    print("6. View Summary")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        attendance.append(0)
        marks.append(0)
        print("Student added successfully")

    elif choice == "2":
        if len(students) == 0:
            print("Add students first")
        else:
            name = input("Enter student name: ")

            if name in students:
                i = students.index(name)
                attendance[i] += 1
                print("Attendance recorded")
            else:
                print("Student not found")

    elif choice == "3":
        name = input("Enter student name: ")

        if name in students:
            i = students.index(name)
            marks[i] = float(input("Enter marks: "))
            print("Marks updated")
        else:
            print("Student not found")

    elif choice == "4":
        name = input("Enter student name: ")

        if name in students:
            event = input("Enter event name: ")
            events.append((name, event))
            print("Event registration successful")
        else:
            print("Student not found")

    elif choice == "5":
        print("Available resources:", resources)
        resource = input("Enter resource name: ")
        quantity = int(input("Enter quantity: "))

        if resource in resources and quantity > 0:
            print(quantity, resource, "allocated successfully")
        else:
            print("Invalid resource or quantity")

    elif choice == "6":
        print("\n--- CAMPUS SUMMARY ---")

        for i in range(len(students)):
            print("Name:", students[i])
            print("Attendance:", attendance[i])
            print("Marks:", marks[i])

        print("Total Students:", len(students))
        print("Event Registrations:", len(events))
        print("Resources:", resources)

    elif choice == "7":
        print("Program ended")
        break

    else:
        print("Invalid choice. Try again.")