import mysql.connector
class Withdrawl:
    def amtWithdrawl(self):
        db=mysql.connector.connect(user='root',password='',host='localhost',database='bankingnew')
        cursor=db.cursor()
        print("<====>WITHDRAWL SECTION<====>\n")
        trt="withdrawl"
        ac=input("YOUR ACCOUNT NUMBER PLEASE:")
        try:
            cursor.execute("SELECT * FROM customerregister WHERE account_number=%s",(int(ac),))
            rs=cursor.fetchall()
            for row in rs:
                f=row[0]
                l=row[1]
                name=f+l
                ty=row[8] 
            op=str(ty)
        except:
            print("SORRY YOU HAVE ENTERED WRONG ACCOUNT NUMBER:")
        if (op == "current"):
            print("HI--->",name)
            print("YOUR HAVING",op,"ACCOUNT")
            print("<==>CURRENT ACCOUNT WITHDRAWL SECTION<==>")
            print("YOUR TRANSACTION DETAILS:\n")
            try:
                cursor.execute("SELECT * FROM currentaccount WHERE account_number=%s",(int(ac),))
                rs=cursor.fetchall()
                for row in rs:
                    amt=float(row[2]) 
                    print("\n")
                    print ("AVAILABLE BALANCE:",amt)
                    print("\n")
                    if(amt==5000):
                        print("SORRY NO MORE TRANSACTION IS ALLOWED:")
                    elif(amt>5000):
                        am=input("ENTER THE AMOUNT TO WITHDRAWL:")
                        new=amt-float(am)
                        print("YOUR NEW BALANCE:",new)
                        cursor.execute("""INSERT INTO transaction(accnum,actype,amount,trtype)
                        VALUES(%s,%s,%s,%s)""",(int(ac),op,float(am),trt))
                        cursor.execute("UPDATE currentaccount SET amount=%s WHERE account_number=%s",(float(new),int(ac)))
                        print("YOUR AMOUNT IS UPDATED SUCCESSFULLY")
                        import options
                        db.commit()
            except:
                print("OOPS! SORRY CHECK YOUR CREDENTIALS:")
                db.close()
                import options
        elif(op == "savings"):
            print("HI--->",name)
            print("YOUR HAVING",op,"ACCOUNT")
            print("<==>SAVINGS ACCOUNT WITHDRAWL SECTION<==>")
            print("YOUR TRANSACTION DETAILS:\n")
            try:
                cursor.execute("SELECT * FROM savingsaccount WHERE account_number=%s",(int(ac),))
                rs=cursor.fetchall()
                for row in rs:
                    amt=float(row[2]) 
                    print("\n")
                    print ("AVAILABLE BALANCE:",amt)
                    print("\n")
                    am=input("ENTER THE AMOUNT TO WITHDRAWL:")
                    new=amt-float(am)
                    if(amt<=50):
                        print("OOPS! SORRY CHECK YOUR ACCOUNT BALANCE")
                    else:
                        print("YOUR NEW BALANCE:",new)
                        cursor.execute("UPDATE savingsaccount SET amount=%s WHERE account_number=%s",(float(new),int(ac)))
                        cursor.execute("""INSERT INTO transaction(accnum,actype,amount,trtype)
                        VALUES(%s,%s,%s,%s)""",(int(ac),op,float(am),trt))
                        print("YOUR AMOUNT IS UPDATED SUCCESSFULLY")
                        db.commit()
                        import options
            except:
                print("OOPS! SORRY CHECK YOUR CREDENTIALS:")
                db.close()
                import options
        else:
            print("KINDLY CHECK YOUR CREDENTIALS:")
            import options
w=Withdrawl
w.amtWithdrawl('self')