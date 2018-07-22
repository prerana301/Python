list1 = []
list2 = ["Maths","Biology","Chemistry","Physics","English","Computer"]
list3 = []

def addData():
    name = input("Enter name:")
    list1.append(name)
    listOfMarks = []
    print("Enter -1 if don't have this module")
    for i in list2:
        marks = int(input("Enter marks in %s: "%i))
        listOfMarks.append(marks)
    list3.append(listOfMarks)
    print("-"*20)
    print("Hello",name,"your marks stored in the data base. Thankyou!!")
    print("-"*20)

def avgMarks():
    name = input("Enter your name:")
    avg = []
    if name in list1:
        index = list1.index(name)
        for i in list3[index]:
            if i != -1:
                avg.append(i)
        avg_marks = sum(avg)/len(avg)
        
        print("Your average marks is: ",avg_marks)
        print("-"*20)
        return name,avg_marks
    else:
        print("There is no such a student")
        print("-"*20)


def avgModule():
    module = input("Enter module name:")
    if module in list2:
        index = list2.index(module)
        col_avg = []
        for i in list3:
            if i[index] != -1:
                col_avg.append(i[index])            
        print(col_avg)
        avg = sum(col_avg)/len(col_avg)
        print("Module average is: ",avg)
        print("-"*20)
        return module,avg
    else:
        print("There is no such a module")
        print("-"*20)
    

while True:
    print("""1. Add data
2. Calculate Average marks of a student
3. Calculate average of module
4. Exit
--------------------------------------------""")
    
    ch = int(input("Enter choice:"))
    print("-"*20)
    if ch == 1:
        addData()
    elif ch == 2:
        avgMarks()
    elif ch == 3:
        avgModule()
    elif ch == 4:
        break
    else:
        print("Invalid input")
        
        
            
        
        
        
        
