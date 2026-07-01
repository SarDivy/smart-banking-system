# Display program title
def title():
    print("=========== Smart Banking System ============")
title()
name=input("Name:")
try:
    balance=int(input("Balance:"))
except ValueError as e:
    print("Wrong Data Input",e)
# Ask the user to choose a transaction
def asking():
    print(" If Deposit money press '1' or If Withdraw money press '2'")
asking()
ask=0
try:
    ask=int(input("Enter Choice:"))
except ValueError:
    print("Invalid Choice!")

# according transaction choose update ypur balance and report
if ask==1 or ask==2:
        if ask==1:
            try:
                def deposit_money():
                    deposit=int(input("Enter Deposit Amount:"))
                    def update_balance(balance,deposit):
                        return balance+deposit
                    a=update_balance(balance,deposit)
                    print("Updated Balance:",a)
                    print("Transaction Successful")
                    print()
                    def report():
                        print("      Final Report       ")
                    report()
                    print("Customer Name:",name)
                    print("Final Balance:",a)
                    print("Transaction Type: Deposit")
                deposit_money()
                
            except ValueError as e:
                print("Invalid Data!",e)
            finally:
                print("Thank you for using Smart Banking System")
            
        elif ask==2:
            try:
                withdraw=int(input("Enter how much money you want to Withdraw:"))
                def withdraw_money(withdraw,balance):
                    if withdraw<=balance:
                        def update_balance(balance,withdraw):
                            return balance-withdraw
                        a=update_balance(balance,withdraw)
                        print("Updated Balance:",a)
                        print("Transaction Successful")
                        print()
                        def report():
                            print("      Final Report       ")
                        report()
                        print("Final Balance:",a)
                        print("Transaction Type: Withdraw")
                    else:
                        print("Insufficient Balance!")
                        
                withdraw_money(withdraw,balance)
                
            except ValueError as e:
                print("Invalid Data!",e)
            finally:
                print("Thank you for using Smart Banking System")
else:
    print("Invalid Data Entry!")
            


            
    

