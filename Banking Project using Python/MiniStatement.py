import mysql.connector
class MiniStatement:
    def miniStatement(self):
        db = mysql.connector.connect(user='root',password='',host='localhost',database='bankingnew')
        cursor = db.cursor()
        print("<====>MINI STATEMENT SECTION<====>\n")
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
            import options
        if (op == "current"):
            print("HI--->",name)
            print("YOUR HAVING",op,"ACCOUNT")
            print("\n<==>CURRENT ACCOUNT MINI-STATEMENT SECTION<==>\n")
            print("YOUR TRANSACTION DETAILS:\n")
            try:
                cursor.execute("SELECT * FROM transaction WHERE accnum=%s",(int(ac),))
                rs=cursor.fetchall()
                for row in rs:
                    acn=int(row[0])
                    act=str(row[1])
                    amount=float(row[2])
                    trstype=str(row[3])
                    print("ACCOUNT NUMBER:",acn)
                    print("ACCOUNT TYPE:",act)
                    print("TYPE OF TRANSACTION:",trstype)
                    print("AMOUNT:",amount)
                    print("\n")
                cursor.execute("SELECT * FROM currentaccount WHERE account_number=%s",(int(ac),))
                rs=cursor.fetchall()
                for row in rs:
                    amt=float(row[2])
                    print ("AVAILABLE BALANCE:",amt,"\n")
                    import options
                    db.commit()
            except:
                print("OOPS! SORRY CHECK YOUR CREDENTIALS:")
                import options
        elif(op == "savings"):
            print("HI--->",name)
            print("YOUR HAVING",op,"ACCOUNT")
            print("\n<==>SAVINGS ACCOUNT MINI-STATEMENT SECTION<==>")
            print("YOUR TRANSACTION DETAILS:\n")
            try:
                cursor.execute("SELECT * FROM transaction WHERE accnum=%s",(int(ac),))
                rs=cursor.fetchall()
                for row in rs:
                    acn=int(row[0])
                    act=str(row[1])
                    amount=float(row[2])
                    trstype=str(row[3])
                    print("ACCOUNT NUMBER:",acn)
                    print("ACCOUNT TYPE:",act)
                    print("TYPE:",trstype)
                    print("AMOUNT:",amount)
                    print("\n")
                cursor.execute("SELECT * FROM savingsaccount WHERE account_number=%s",(int(ac),))
                rs=cursor.fetchall()
                for row in rs:
                    amt=float(row[2]) 
                    print("\n")
                    print ("AVAILABLE BALANCE:",amt,"\n")
                    import options
                    db.commit()
            except:
                print("OOPS! SORRY CHECK YOUR CREDENTIALS:")
                import options
        else:
            print("YOU HAVE ENTERED WRONG OPTION")
            import options
m=MiniStatement
m.miniStatement('self')