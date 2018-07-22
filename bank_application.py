dict1 = {}
while True:
    list1 = ["Name","Address","Age","Account Type","Amount"]
    list2 = []
    
    ch = int(input("1 . New Customer\n2 . Existing Customer\n3 . Exit\nEnter your choice:" ))
    if ch == 1:
        for i in list1:
            list2.append(input("Enter %s: "%i))
        acc_num = input("Enter account number:")
        dict1[acc_num] = dict(zip(list1,list2))

    elif ch == 2:
        acc_num = input("Enter account number:")
        if acc_num in dict1:
            print("Record Found")
            ch = int(input("1 . Check Balance\n2 . Withdraw\n3 . Deposite\nEnter your choice: "))
            if ch == 1:
                print("Yor available balance is:",dict1[acc_num]["Amount"])
            elif ch == 2:
                w_amt = int(input("Enter amount to be withdrawn:"))
                dict1[acc_num]["Amount"] = int(dict1[acc_num]["Amount"]) - w_amt
                print("Withdraw succesfull !! your balance is:",dict1[acc_num]["Amount"])
                
            elif ch == 3:
                d_amt = int(input("Enter amount to be deposite:"))
                dict1[acc_num]["Amount"] = int(dict1[acc_num]["Amount"]) + d_amt
                print("Deposite succesfull !! your balance is:",dict1[acc_num]["Amount"])

    elif ch == 3:
            break

    else:
            print("Invalid input")
                
                
                
            
        
            
        
