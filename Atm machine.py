import time
print("please insert your Card")
time.sleep(5)
password=12345
pin=int(input("Enter your pin"))
balance=1000
if pin==password:
    while True:
        print("""
        1.Balance
        2.Withdraw balnce
        3.Deposit Balance
        4.Exit
        """)
        try:
            option=int(input("please enter your choice :"))
        except:
            print("please enter valid option")

        if option==1:
            print(f"Your balance is {balance}")

            print("**************************************************")
            print("**************************************************")
        if option==2:
            withdraw_amount=int(input("Please enter withdraw amount:"))

            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your current balance is {balance}")

            print("**************************************************")
            print("**************************************************")
        if option==3:
            deposit_amount=int(input("Please enter amount to be deposited:"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is{balance}")

            print("**************************************************")
            print("**************************************************")

        if option==4:
            break
