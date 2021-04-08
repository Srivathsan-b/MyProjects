import mysql.connector
class DetailsUpdate:
    def detailsUpdate(self):
        db = mysql.connector.connect(user='root',password='',host='localhost',database='bankingnew')
        cursor = db.cursor()
        print("<====>DETAILS UPDATION SECTION<====>\n")
        ac=input("ACCOUNT NUMBER REQUIRED HERE:\n")
        try:
            cursor.execute("SELECT * FROM customerregister WHERE account_number=%s",(ac,))
            rs=cursor.fetchall()
            for row in rs:
                fn=row[0]
                ln=row[1]
                ad1=row[2]
                ad2=row[3]
                ct=row[4]
                st=row[5]
                pin=row[6]
                acc=row[7]
            print("HI....",fn+ln,"\n")
            print("<====>YOUR EXISTING DETAILS<====>\n")
            print("FIRST NAME:",fn)
            print("LAST NAME:",ln)
            print("ADDRESS 1:",ad1)
            print("ADDRESS 2:",ad2)
            print("CITY:",ct)
            print("STATE:",st)
            print("PINCODE:",int(pin))
            print("ACCOUNT NUMBER:",int(acc))
            print("\nLIST OF OPTIONS TO CHANGE YOUR DATAS\n")
            print("1.FIRST NAME:")
            print("2.LAST NAME:")
            print("3.ADDRESS 1:")
            print("4.ADDRESS 2:")
            print("5.CITY:")
            print("6.STATE:")
            print("7.PINCODE:")
            opt=input("\nYOUR OPTION HERE>:---->")
            if(opt=="1"):
                op1=input("FIRST NAME HERE:---->")
                cursor.execute("UPDATE customerregister SET fname=%s WHERE account_number=%s",(op1,int(ac)))
                print("FIRST NAME UPDATED SUCCESSFULLY:")
            elif(opt=="2"):
                op1=input("LAST NAME HERE:---->")
                cursor.execute("UPDATE customerregister SET lname=%s WHERE account_number=%s",(op1,int(ac)))
                print("LAST NAME UPDATED SUCCESSFULLY:")            
            elif(opt=="3"):
                op1=input("ADDRESS 1 HERE:---->")
                cursor.execute("UPDATE customerregister SET address1=%s WHERE account_number=%s",(op1,int(ac)))
                print("ADDRESS 1 UPDATED SUCCESSFULLY:")
            elif(opt=="4"):
                op1=input("ADDRESS 2 HERE:---->")
                cursor.execute("UPDATE customerregister SET address2=%s WHERE account_number=%s",(op1,int(ac)))
                print("ADDRESS 2 UPDATED SUCCESSFULLY:")
            elif(opt=="5"):
                op1=input("CITY HERE:---->")
                cursor.execute("UPDATE customerregister SET city=%s WHERE account_number=%s",(op1,int(ac)))
                print("CITY UPDATED SUCCESSFULLY:") 
            elif(opt=="6"):
                op1=input("STATE HERE:---->")
                cursor.execute("UPDATE customerregister SET state=%s WHERE account_number=%s",(op1,int(ac)))
                print("STATE UPDATED SUCCESSFULLY:") 
            elif(opt=="7"):
                op1=input("PINCODE HERE:---->")
                cursor.execute("UPDATE customerregister SET pincode=%s WHERE account_number=%s",(int(op1),int(ac)))
                print("PINCODE UPDATED SUCCESSFULLY:")
            else:
                print("<*-*-*>  YOU HAVE ENTERED WRONG OPTION  <*-*-*>")      
        except:
            print("OOPS! CHECK YOUR ACCOUNT NUMBER:")
            import options
d=DetailsUpdate
d.detailsUpdate('self')