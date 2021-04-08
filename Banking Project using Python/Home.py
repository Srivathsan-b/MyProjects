class Home:
    def chooseOption(self):
        print("WELCOME TO BANKING:\n")
        print("1.SIGN IN:")
        print("2.SIGN UP:")
        print("3.ADMIN LOGIN:")
        print("4.QUIT:\n")
        op=input("YOUR OPTION HERE:")
        if op=="1":
            import Login
        elif(op=="2"):
            import SignUp
        elif(op=="3"):
            import AdminLogin
        elif(op=="4"):
            raise SystemExit
        else:
            print("YOU HAVE ENTERED WRONG OPTION:")
h=Home
h.chooseOption('self')