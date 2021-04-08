import mysql.connector
from random import randint
class Signup: 
    def readDetails(self):
        db = mysql.connector.connect(user='root',password='',host='localhost',database='bankingnew')
        cursor = db.cursor()
        ac=int(randint(40005000, 60007000)) 
        print("REGISTER YOUR DETAILS HERE:\n")
        f=input("FIRST NAME---->")
        l=input("LAST NAME---->")
        a1=input("ADDRESS 1---->")
        a2=input("ADDRESS 2---->")
        c=input("CITY---->")
        s=input("STATE---->")
        p=input("PINCODE---->")
        p1=str(p)
        if(p1.isdigit()):
            p2=len(p1)
            ln=int(p2)   
            if (ln==6):
                p=p
            else:
                print("SHOULD CONTAINS 6 DIGITS:")
                p=input("RETYPE YOUR PINCODE---->")
        else:
            print("YOU SHOULD ENTER DIGITS ONLY:")
            p=input("RETYPE YOUR PINCODE---->")   
        pw1=input("PASSWORD:---->")
        pw2=input("RETYPE PASSWORD:")
        pk1=str(pw1)
        pk2=str(pw2)
        l1=int(len(pk1))
        l2=int(len(pk2))
        if(l1 == 8 & l2 == 8):
            if (pw1 == pw2):
                if(pw1.isalnum()):
                    pw1=pw2
                else:
                    print("YOUR PASSWORD SHOULD CONTAINS ALPHABETS AND DIGITS:")
                    pw1=input("PASSWORD:---->")
            else:
                print("BOTH PASSWORDS SHOULD MATCH:")
                pw1=input("RE TYPE YOUR PASSWORD:---->")
        else:
            print("YOUR PASSWORD SHOULD BE IN LENGTH 8:")
            pw1=input("RE TYPE YOUR PASSWORD:---->")
        usr=f+l
        print("\n")
        try:
            print("A.CURRENT ACCOUNT:")
            print("B.SAVINGS ACCOUNT:")
            print("\n")
            option=input("YOUR CHOICE:")
            if (option == 'a'):
                print("<====>CURRENT ACCOUNT SYSTEM<====>:")
                print("BY PAYING JUST 5K TO OPEN YOUR NEW ACCOUNT")
                amt=input("PAY HERE:")
                if(int(amt)==5000):
                    t="current"
                    cursor.execute("""INSERT INTO currentaccount(customername,account_number,amount)
                    VALUES(%s,%s,%s)""",(usr,int(ac),float(amt)))
                    cursor.execute("""INSERT INTO customerregister(fname,lname,address1,address2,city,state,pincode,account_number,actype)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(f,l,a1,a2,c,s,int(p),int(ac),t))
                    cursor.execute("""INSERT INTO customerlogin(password,accnum)
                    VALUES(%s,%s)""",(pw1,int(ac)))
                    print("YOUR ACCOUNT WAS CREATED SUCCESSFULLY")
                    print("YOUR ACCOUNT NUMBER & CUSTOMER ID:---->\t",ac)
                    print("YOUR PASSWORD:---->\t",pw1)
                    db.commit()
                    print("\nLOGIN INTO YOUR ACCOUNT:")
                    import Login
                else:
                    print("ATTENTION 5000 REQUIRED:")
                    raise SystemExit               
            elif (option == 'b'):
                a=0
                t="savings"
                print("<====>SAVINGS ACCOUNT SYSTEM<====>:")
                print("\n")
                print("CREATE YOUR ACCOUNT WITH ZERO BALANCE")
                cursor.execute("""INSERT INTO savingsaccount(customername,account_number,amount)
                VALUES(%s,%s,%s)""",(usr,int(ac),float(a)))
                cursor.execute("""INSERT INTO customerregister(fname,lname,address1,address2,city,state,pincode,account_number,actype)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(f,l,a1,a2,c,s,int(p),int(ac),t))
                cursor.execute("""INSERT INTO customerlogin(password,accnum)
                VALUES(%s,%s)""",(pw1,int(ac)))
                print("\n")
                print("YOUR ACCOUNT WAS CREATED SUCCESSFULLY")
                print("YOUR ACCOUNT NUMBER & CUSTOMER ID:---->\t",ac)
                print("YOUR PASSWORD:---->\t",pw1)
                db.commit()
                print("\nLOGIN INTO YOUR ACCOUNT:")
                import Login
            else:
                print("YOU HAVE ENTERED WRONG OPTION") 
                db.close()  
                import Home  
        except:
            print("YOU HAVE GIVEN INCORRECT DATAS:")
            db.close()
            import Home
s=Signup
s.readDetails('self')