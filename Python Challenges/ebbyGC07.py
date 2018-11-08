def withdraw(amount,c_balance):
    if amount%5 != 0:
        return False
    elif amount + 0.5 > c_balance:
        return False
    new_balance = c_balance - amount - 0.5
    return new_balance
