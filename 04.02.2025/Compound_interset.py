def compound_interest(principal, rate, time):
    amount = principal * (pow((1 + rate / 100), time))
    CI = amount - principal
    print("The compound interest is",CI)
compound_interest(10000, 10.25, 5)
