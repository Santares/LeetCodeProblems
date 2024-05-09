if __name__ == '__main__':

    x = 30000
    y = 0.009
    z = 36

    t = y/12

    s = (x * t) / (1 - (1+t)**(-1*z))
    print(s)

    totalWithLoan = s * z
    print(totalWithLoan)

    money = x
    interest = 0
    bank = 0.04
    bankRate = bank/12
    for i in range(z):
        money -= s
        interest += money * bankRate
        money += money * bankRate
    print(interest)

    money = x
    for i in range(z):
        money -= s
        money += money * bankRate
    print(money)

    money = x
    for i in range(z):
        # money -= s
        # interest += money * bank
        money += money * bankRate
    print(money)

    money = x
    for i in range(3):
        money *= 1 + bank
    print(money)
