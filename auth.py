# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

# Initializing the system
import random
import validation
import database
from getpass import getpass

user = {
  # 9032874196:['seyi', 'onifade', 'seyi@zuri.teams', 'passwordseyi'],
  # 6437587453:['mike', 'zuri', 'mike@zuri.teams', 'passwordmike'],
  # 9389360360:['love', 'zuri', 'love@zuri.teams', 'passwordlove'],
   8005046643:['green', 'man', 'greenman', 'greenman@zuri.teams', 'password']}

def init():
    print("Welcome to Rip-off bank")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
   # print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()

    elif selected_option == 2:

        withdrawal_operation()

    elif selected_option == 3:

        logout()

    elif selected_option == 4:

        exit()

    else:

        print("Invalid option selected")

        bank_operation(user)


def withdrawal_operation():

    print("withdrawal")
    # get current balance\

    currentBalance =  get_current_balance(['green','man','greenman@zuri.teams','password',0])

    print('Your current balance is {}'.format(currentBalance))
    # get amount to withdraw


    withdrawalAmount = int(input('How much would you like to withdraw?\n'))

    if withdrawalAmount > currentBalance:

        print('Dear customer your balance is too low to perform this transaction. Please enter a valid amount')
    else:

        print(' Please take your cash ({}).'.format(withdrawalAmount))

        Deduct = currentBalance - withdrawalAmount

        print('Your new balance is {}'.format(Deduct))

    anythingElse = int(input('Would you like to perform another transaction: 1(Yes) 2(No)\n'))  

    if anythingElse == 1:

        bank_operation(8005046643)

    else:
            
            print('Thanks for banking with us')  
            login()    

    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def deposit_operation():

    print("Deposit Operations")

    # get current balance
    currentBalance = get_current_balance(['green','man','greenman@zuri.teams','password',0])

    print('Your current balance is {}'.format(currentBalance))

    # get amount to deposit
    depositAmount = int(input('How much would you like to deposit?\n'))

    addition = currentBalance + depositAmount

    print ('Thanks for banking with us,your current balance is now {}'.format(addition))

    anythingElse = int(input('Would you like to perform another  transaction: 1(yes) 2(No)\n'))

    if anythingElse == 1:

        bank_operation(8005046643)

    else:
        print('Thanks for banking with us. Stay safe and work hard so we can keep collecting your hardearned cash')    
    
        # add deposited amount to current balance
    # display current balance

def generation_account_number():

    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]

def logout():
    
    login()

def exit():

    init()

init()
