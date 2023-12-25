transactions_in_cents = [1000, -450, 7500, -3475, 13000, -8150, 25000, -850, 0, -1125,
                         -600, 102550, -25025, 6500, -3850, -2500, 1875, 4000]
print("Transactions (cents):")
print(transactions_in_cents)

transactions = [transaction / 100 for transaction in transactions_in_cents]

print("Transactions (dollars)")
print(transactions)

transactions.sort()

print("Sorted Transactions")
print(transactions)

deposits = [transaction for transaction in transactions if transaction >= 0]
withdrawals = [transaction for transaction in transactions if transaction < 0]

print("Deposits:")
print(deposits)
print("Withdrawals:")
print(withdrawals)


def invert_negative_num(negative_num):
    positive_num = -1 * negative_num
    return positive_num


withdrawals = [invert_negative_num(withdrawal) for withdrawal in withdrawals]
print(withdrawals)

largest_withdrawals = withdrawals[:5]
print("Largest Withdrawals")
print(largest_withdrawals)

average_deposit = sum(deposits) / len(deposits)
average_deposit = int(average_deposit)

average_withdrawal = sum(withdrawals) / len(withdrawals)
average_withdrawal = int(average_withdrawal)

print("Average Deposit (int):")
print(average_deposit)
print("Average Withdrawal (int):")
print(average_withdrawal)

# Great work using your ever-improving Python skills to organize and analyze bank transactions!
# During this project you converted transactions from cents to dollars, sorted them,
# created new lists of deposits, withdrawals, and largest withdrawals, and calculated
# average transactions and final account balance. Along the way, you used list comprehensions
# to create modified and filtered lists, and practiced with type casting and slice notation.

balance = sum(transactions)
print(balance)
