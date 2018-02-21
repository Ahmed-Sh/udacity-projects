if __name__ == "__main__":
    # Code below  to prevent Error in Python 2
    if hasattr(__builtins__, 'raw_input'):
        input = raw_input


    def atm(request, balance):
        """ atm function show money process in ATM """
        cash_list = [200, 100, 50, 20, 10, 5]
        errors = ['You have not Enough Money, your balance is : {} Pound'
                  , 'You Request Nothing, your balance is : {} Pound']
        if request > balance:
            print(errors[0].format(balance))
        elif request <= 0:
            print(errors[1].format(balance))
        else:
            for cash in cash_list:
                while request >= cash:
                    print('give {}'.format(cash))
                    request -= cash
            print('Your process if finished..')

    money = int(input("Enter Your request money : "))
    atm(money, 2000)
