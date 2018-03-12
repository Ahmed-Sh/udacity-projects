if __name__ == "__main__":
    from time import ctime, sleep

    class ATM:
        """ Withdraw process from multiple ATMs"""

        def __init__(self, balance, bank_name):
            self.balance = balance
            self.bank_name = bank_name
            self.withdrawal_list = []
            self.withdrawal_time = []
            self.cash_list = [100, 50, 20, 10, 5, 2, 1]

        def withdraw(self, request):
            print('***********************************************')
            print(f'Welcome to {self.bank_name}')
            print('Current balance : {}'.format(self.balance))
            print('***********************************************')

            if request > self.balance:
                print('You have not Enough Money. Your balance is : {}'.format(self.balance))

            elif request <= 0:
                print('You ask nothing. You balance is : {}'.format(self.balance))

            else:
                ATM.withdraw_process(self, request)

            print('***********************************************')
            return self.balance

        def withdrawals(self):
            i = 1
            for amount, time in zip(self.withdrawal_list, self.withdrawal_time):
                print('Date & Time : ' + str(time) + '\nWithdrawal ({}): '.format(i) + str(amount))
                i += 1
                print('***********************************************')

        def withdraw_process(self, request):
            self.balance -= request
            self.withdrawal_list.append(request)
            self.withdrawal_time.append(str(ctime()))
            for cash in self.cash_list:
                while request >= cash:
                    print('give : {}'.format(cash))
                    request -= cash

            print("Balance remain : {}".format(self.balance))

    atm1_balance = 2000
    atm1_bank = 'Ahly Bank'
    atm1 = ATM(atm1_balance, atm1_bank)
    atm1.withdraw(500)
    sleep(2)
    atm1.withdraw(200)
    sleep(2)
    atm1.withdraw(400)
    atm1.withdrawals()

    # atm2_balance = 1000
    # atm2_bank = 'Bank Misr'
    # atm2 = ATM(atm2_balance, atm2_bank)
    # atm2.withdraw(500)
    # atm2.withdraw(150)
    # atm2.withdraw(150)
