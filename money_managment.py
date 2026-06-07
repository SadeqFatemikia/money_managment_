import time


class User:

    def __init__(self, full_name, total):
        self.full_name = full_name
        self.total = total

    def default_managment(self):
        """
        In this method we divided total money to 50 30 20
        --50 : is our main account
        --30: we consider this bank account for SHOPPING  OR EXTRA SERVICES (include : gym membership , any video platform, trip)
        --20 : we consider this bank account for  INVESTING & SAVE
        """
        main_account = self.total * 0.5
        shopping_account = self.total * 0.3
        investing_account = self.total * 0.2
        print('*' * 5)
        print(
            f'Your budget for\n \t Main Account:{main_account} \n \t Shopping Account:{shopping_account} \n \t Investing Account:{investing_account} ')
        return f'Your budget for\n \t Main Account:{main_account} \n \t Shopping Account:{shopping_account} \n \t Investing Account:{investing_account} '

    def recomend_managment(self):
        """
        In this method we divided total money to 80 20 20
        --80 : is our main account
        --20: we consider this bank account for SHOPPING  OR EXTRA SERVICES (include : gym membership , any video platform, trip)
        --20 : we consider this bank account for  INVESTING & SAVE
        """
        main_account = self.total * 0.8
        shopping_account = self.total * 0.2
        investing_account = self.total * 0.2
        print('*' * 5)
        print(
            f'Your budget for\n \t Main Account:{main_account} \n \t Shopping Account:{shopping_account} \n \t Investing Account:{investing_account} ')
        return f'Your budget for\n \t Main Account:{main_account} \n \t Shopping Account:{shopping_account} \n \t Investing Account:{investing_account} '

    def show(self):
        # show last amount money
        pass

    def make_note_file(self):
        with open('moneyManagment.txt', 'w') as file:
            file.write(str(self.total))


print('*' * 30)
print('*' * 20)
print('*' * 10)
print('\tHello to our money manager script \n \tPlease enter your money managment choice ')
print('*' * 30)
print('*' * 20)
print('*' * 10)
a = time.sleep(3)
try:

    user_fullname = str(input("Enter full name: "))
    user_upper_name = user_fullname.upper()
    print(f'Hello \t-{user_upper_name}-\t Please enter your Total Money. ')
    user_total = int(input("Enter total money: "))
    print(
        f'\nWe have two kind of money managment \n\t1:\n\t50: Main Account\n\t30:Shopping Account \n\t20:Investing Account \n *** \n\t2:\n\t80:Main Account \n\t20:Shopping Account\n\t20:Investing Account')

    user_choice = int(int(input("\nEnter your choice: ")))
    u1 = User(user_fullname, user_total)
    print('Your choice is:', user_choice)
    print('Wait...')
    a=time.sleep(1)

    if user_choice == 1:
        u1.default_managment()


    elif user_choice == 2:
        u1.recomend_managment()
    else:
        print("Invalid choice")
        re_enter = user_choice

    a = str(input('Do you want to save money managment as a text file? (y/n):'))
    if a == 'y':
        with open('moneyManagment.txt', 'w') as file:
            if user_choice == 1:
                file.write(str(u1.default_managment()))
            elif user_choice == 2:
                file.write(str(u1.recomend_managment()))
    else:
        print('Ok -\tAs you wish')

except TypeError:
    print("Please enter your full name ")

finally:
    print("Goodbye")
