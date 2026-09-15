#atm program
bal=10000
pin=int(input("enter your pin"))
if(pin==1234):
    while True:
        print("press 1 for bal enquiry")
        print("press 2 for add money")
        print("press 3 for withraw")
        print("press 4 for pin")
        print("pess 5 for exit")
        choice=int(input("enter your choice"))
        if(choice==1):
            print("your bal is",bal)
        elif(choice==2):
            b=int(input("enter a amount"))
            bal+=b 
            print(bal)
        elif(choice==3):
            amount=int(input("enter a amount"))
            if amount>+bal:
                print("insufficent balance")
            else:
                bal-=amount
                print(bal)
        elif(choice==4):
            old_password=int(input("enter a old paasword"))
            if (old_password==1234):
                new_password=int(input("enter a new password"))
                confirm_password=int(input("enter a confirm paasword"))
                if(new_password==confirm_password):
                    print("your password change sucessfully")
                elif (new_password!=confirm_password):
                    print("new password and confirm password are not matched")
                else:
                    print("incorrect old password")
            elif(choice==5):
                print("thank you for visting")
                exit()

                  
                    
                
    

