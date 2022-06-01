#Login form
import mysql.connector
class Login:
    def custlogin(self):
        db = mysql.connector.connect(user='root',password='',host='localhost',database='bankingnew')
        cursor = db.cursor()
        print("<====>CUSTOMER LOGIN<====>:\n")
        print("\n")
        acc=input("CUSTOMER ID HERE---->:")
        pwd=input("PASSWORD HERE---->:")
        try:
            cursor.execute("SELECT * FROM customerlogin WHERE accnum=%s AND password=%s",(int(acc),pwd))
            rs=cursor.fetchall()
            for row in rs:
                pwd=row[0]
                acc=row[1]
            cursor.execute("SELECT * FROM customerregister WHERE account_number=%s",(int(acc),))
            rst=cursor.fetchall()
            for row in rst:
                f=row[0]
                l=row[1]
                act=row[8]
                name=f+l
                print("\nWELCOME",name,"TO OUR BANK")
                print("YOU ARE HAVING",act,"ACCOUNT IN OUR BANK")
                import options
                db.commit()
        except:
            print("YOUR USERNAME OR PASSWORD IS INVALID::")
            import Home
            db.close()   
sn=Login
sn.custlogin('self')