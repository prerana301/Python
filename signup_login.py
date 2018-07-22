# Cretaing user name and password

dict1 = {}
while True:
    print("1 . Sign Up")
    print("2 . Login")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        name = input("Enter name:")
        pwd = input("Enter password:")
        dict1[name]= pwd
        print("Account Created")
        print(dict1)
    elif ch == 2:
        name = input("Enter name:")
        if name in dict1.keys():
            print("name is available in the records")
            pwd = input("Enter password:")
            if dict1[name] == pwd:
                print("Login Succesfull")
            else:
                print("Invalid Password")
        else:
            print("Invalid Name")





















