if __name__ == "__main__":

    # Prevent Python 2 from raise Error
    if hasattr(__builtins__, 'raw_input'):
        input = raw_input


    def withdraw(request, balance):
        """ make multiple withraw """
        cash_list = [100, 50, 20, 10, 5, 2, 1]
        if request > balance:
            print(" You have not Enough Money. Your balance is : {}".format(balance))
        elif request <= 0:
            print("You ask nothing. You balance is : {}".format(balance))

        else:
            balance -= request
            for cash in cash_list:
                while request >= cash:
                    print('give : {}'.format(cash))
                    request -= cash

            print("Balance remain : {}".format(balance))

        return balance


    balance = 2000
    request = int(input("Enter request money : "))
    while balance > request:
        balance = withdraw(request, balance)
        request = int(input("Enter request money : "))

    balance = withdraw(request, balance)
