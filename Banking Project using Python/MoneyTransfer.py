import mysql.connector
class MoneyTransfer:
    def moneyTransfer(self):
        db = mysql.connector.connect(user='root',password='',host='localhost',database='bankingnew')
        cursor = db.cursor()
        print("<====> MONEY TRANSFER SECTION <====>\n")
        trt="money_transfer"
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
        try:
            if(op=="current"):
                print("HI--->",name)
                print("YOUR HAVING",op,"ACCOUNT")
                print("<====>CURRENT ACCOUNT MONEY TRANSFER SECTION:<====>\n")
                cursor.execute("SELECT * FROM currentaccount WHERE account_number=%s",(int(ac),))
                rs=cursor.fetchall()
                for row in rs:
                    samt=row[2] 
                print("YOUR AVAILABLE BALANCE IS:",samt,"\n")
                racn=input("ACCOUNT NUMBER HERE:")
                cursor.execute("SELECT * FROM currentaccount WHERE account_number=%s",(int(racn),))
                rs=cursor.fetchall()
                for row in rs:
                    ramt=row[2]
                trs=input("AMOUNT TO TRANSFER:")
                if(trs==samt):
                    print("SORRY YOU CAN'T PERFORM THIS ACTION")
                    import options
                else:
                    strs=float(samt)-float(trs)
                    cursor.execute("UPDATE currentaccount SET amount=%s WHERE account_number=%s",(float(strs),ac))
                    recv=float(trs)+float(ramt)   
                    cursor.execute("UPDATE currentaccount SET amount=%s WHERE account_number=%s",(float(recv),racn))
                    cursor.execute("""INSERT INTO transaction(accnum,actype,amount,trtype)
                    VALUES(%s,%s,%s,%s)""",(int(ac),op,float(trs),trt))
                    print("YOUR MONEY TRANSFER COMPLETED SUCCESSFULLY:\n")
                    print("GO AND CHECK YOUR ACCOUNT BALANCE (MINI-STATEMENT):")
                    import options
            elif(op=="savings"):
                print("HI--->",name)
                print("YOUR HAVING",op,"ACCOUNT")
                print("<====>SAVINGS ACCOUNT MONEY TRANSFER SECTION:<====>\n")
                cursor.execute("SELECT * FROM savingsaccount WHERE account_number=%s",(int(ac),))
                rs=cursor.fetchall()
                for row in rs:
                    samt=row[2] 
                print("YOUR AVAILABLE BALANCE IS:",samt,"\n")
                racn=input("ACCOUNT NUMBER HERE:")
                cursor.execute("SELECT * FROM savingsaccount WHERE account_number=%s",(int(racn),))
                rs=cursor.fetchall()
                for row in rs:
                    ramt=row[2]
                trs=input("AMOUNT TO TRANSFER:")
                if(trs==samt):
                    print("SORRY YOU CAN'T PERFORM THIS ACTION")
                    import options
                else:
                    strs=float(samt)-float(trs)
                    cursor.execute("UPDATE savingsaccount SET amount=%s WHERE account_number=%s",(float(strs),ac))
                    recv=float(trs)+float(ramt)    
                    cursor.execute("UPDATE savingsaccount SET amount=%s WHERE account_number=%s",(float(recv),racn))
                    cursor.execute("""INSERT INTO transaction(accnum,actype,amount,trtype)
                    VALUES(%s,%s,%s,%s)""",(int(ac),op,float(trs),trt))
                    print("YOUR MONEY TRANSFER COMPLETED SUCCESSFULLY:\n")
                    print("GO AND CHECK YOUR ACCOUNT BALANCE (MINI-STATEMENT):")
                    import options
        except:
            print("CHECK YOUR ACCOUNT NUMBER:")
            import options
m=MoneyTransfer
m.moneyTransfer('self')