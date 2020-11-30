def login(sign):
    if sign=='sign in':
        detail=open('login.txt','r')
        sente=open('login1.txt','r')
        acc=input("Enter your account id-")
        pas=input("Enter your password-")
        
        det=str(detail.read())
        sen=str(sente.read())

        if acc==det:
            if pas==sen:
                print("Successfully signed in")
            else:
                print("Password is wrong")
        else:
            print("Account id is wrong")

        detail.close()
        sente.close()



    elif sign=='sign of':
        detail=open('login.txt','w')
        sente=open('login1.txt','w')
        
        detail.truncate()
        sente.truncate()

        detail.write(input("Create an account id"))
        sente.write(input("Create password"))
        print("Account successfully created.")
    else:
        print("Only sign in supported")
login(input("Want to sign in or sign of"))