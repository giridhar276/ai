class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdrawal = 1500
try:
    if withdrawal > balance:
        raise InsufficientBalanceError("Insufficient account balance")
except InsufficientBalanceError as error:
    print(error)
