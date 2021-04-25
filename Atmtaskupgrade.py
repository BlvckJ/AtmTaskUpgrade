import random

database={}


def init():
    validOption=False
    print('Welcome to Apex Bank Inc')

    while validOption==False:

     accountHolder= int(input('Do you have an account with us : 1 (yes) 2 (no)\n'))

    if(accountHolder==1):
        validOption=True
        login()
    elif(accountHolder ==2):
         validOption=True
         register()
    else:
     print('You have selected an invalid option')


def login():
    print('This is the login option')

def register():
        print('This is the register function')

def bankoperations():
            print('Bank Operations')

def generateAccountNumber():

                print('Generating Account Number')
                return random.randrange(1111111111,9999999999)

                


print(generateAccountNumber())
            
#init()

login()

register()

bankoperations()

generateAccountNumber()
