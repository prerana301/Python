# employee details

dict1 = {}

while True:
    list1 = ["Name","Address","Salary","Age","phone"]
    list2 = []
    ch = int(input("1 . Add Data\n2 . Show Data\n3 . Exit\nEnter your choice:"))
    if ch == 1:
        print("\n****** Enter Data For New Employe ******\n")
        for item in list1:
            list2.append(input("Enter %s: "%item))
        emp_id = input("\nCreate Emp ID:")
        dict1[emp_id] = dict(zip(list1,list2))
        print("\n****** Data added ******\n")
        
    elif ch == 2:
        print("\n****** Get Employee Details Here ******")
        emp_id = input("\nEnter emp id: ")
        if emp_id in dict1:
            print("\n****** Record Found ******\n")
            print("\n",dict1[emp_id])
        else:
            print("\n****** Record not found *****\n")

    elif ch == 3:
        break

    else:
        print("Invalid Input")


        
