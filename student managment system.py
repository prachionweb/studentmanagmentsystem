import csv

filename = "student managment.py.csv"

while True:
    print("\n----- Student Management System -----")
    print("Press 1 for view student")
    print("Press 2 for add student")
    print("Press 3 for add course")
    print("Press 4 for update student")
    print("Press 5 for delete student")
    print("Press 6 for exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

    elif choice == 2:
        rollno = int(input("Enter your roll no: "))
        name = input("Enter your name: ")
        percentage = float(input("Enter your percentage: "))
        course = input("Enter your course: ")
        state = input("Enter your state: ")

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([rollno, name, percentage, course, state])

        print("Student added successfully")

    elif choice == 3:
        course = input("Enter your course: ")

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["COURSE", course])

        print("Course added successfully")

    elif choice == 4:
        rollno = int(input("Enter your roll no to update: "))

        rows = []
        updated = False

        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) >= 5 and row[0].isdigit() and int(row[0]) == rollno:
                    print("Student found successfully")

                    row[1] = input("Enter your new name: ")
                    row[2] = input("Enter your new percentage: ")
                    row[3] = input("Enter your new course: ")
                    row[4] = input("Enter your state: ")

                    updated = True

                rows.append(row)

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if updated:
            print("Student updated successfully")
        else:
            print("Student not found")

    elif choice == 5:
        rollno = int(input("Enter your roll no for delete details: "))

        rows = []
        deleted = False

        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) >= 1 and row[0].isdigit() and int(row[0]) == rollno:
                    deleted = True
                else:
                    rows.append(row)

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if deleted:
            print("Data deleted successfully")
        else:
            print("Data not found")

    elif choice == 6:
        print("Thank you")
        break

    else:
        print("Invalid choice")
print("hello world")