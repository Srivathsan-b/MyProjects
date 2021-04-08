class Options:
    def chooseOpt(self):
        print("\n<====>OPERATIONS<====>\n")
        print("1.DEPOSIT:")
        print("2.WITHDRAWL:")
        print("3.MINI-STATEMENT:")
        print("4.MONEY-T-RANSFER:")
        print("5.DETAILS-UPDATION")
        print("6.ACCOUNT-CLOSURE:")
        print("7.EXIT:\n")
        opt=input("YOUR CHOICE:")
        if (opt=="1"):
            import Deposit
        elif(opt=="2"):
            import Withdrawl
        elif(opt=="3"):
            import MiniStatement
        elif(opt=="4"):
            import MoneyTransfer
        elif(opt=="5"):
            import DetailsUpdate
        elif(opt=="6"):
            import AccountClosure
        elif(opt=="7"):
            print("THANKS FOR THE BANKING:")
            raise SystemExit
        else:
            print("\n<*/*/*/*> YOU HAVE ENTERED WRONG CHOICE <*/*/*/*>")
o=Options
o.chooseOpt('self')