# calculate balance the same way as in proj. 2 
        
def calc_balance(income,expenses):
    balance = income - expenses
    return balance

# print a message based on given balance similiar to proj 3

def financial_status(balance):
    if balance > 0:
        print("Great! You're saving money!")
    elif balance == 0:
        print("You're breaking even.")
    elif balance < 0:
        print("***WARNING***\nYou're overspending!")
    return balance