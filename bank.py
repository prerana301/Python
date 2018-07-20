# bank application

data = {}
list1 = ["Name", "Address", "Account Type", "Amount"]

def addData():
    list2 = []
    for i in list1:
        d1 = input("Enter %s:" %i)
        list2.append(d1)
    return list2
while True:
    ch = int(input("1.New Customer\n2.Existing Customer\nEnter Choice:"))
    if ch == 1:
        list2 = addData()
        acc_num = int(input("Enter account number:"))
        data[acc_num] = dict(zip(list1, list2))
        print(data)

    elif ch == 2:
        acc_num = int(input("Enter account number:"))
        if acc_num in data:
            print("*********Record Found********")
            ch = int(input("1.Check Balance\n2.Withdraw\n3.Deposit\nEnter Choice:"))
            if ch == 1:
                print("Available Balance:",data[acc_num]["Amount"])
            elif ch == 2:
                w = int(input("How much you want to withdraw:"))
                w1 = int(data[acc_num]["Amount"])-w
                print("Money withdraw successfull, remaining balance:",w1)
                data[acc_num]["Amount"] = w1
            elif ch == 3:
                w = int(input("How much you want to deposite:"))
                w1 = int(data[acc_num]["Amount"])+w
                print("Deposite Successfull, Available Balance:",w1)
                data[acc_num]["Amount"] = w1
        else:
            print("Record Not Found")

    elif ch == 3:
        break

    else:
        print("Invalid choice")