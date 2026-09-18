expenseoffood=int(input("Enter your expense of food: "))
expenseoftravel=int(input("Enter your expense of travel: "))
expenseofshopping=int(input("Enter your expense of shopping: "))
def total(expenseoffood,expenseoftravel,expenseofshopping):
    totalexpense=(expenseoffood+expenseoftravel+expenseofshopping)
    return totalexpense
def highestexpense(expenseoffood,expenseoftravel,expenseofshopping):
    if expenseoffood > expenseoftravel and expenseoffood > expenseofshopping:
        maxexpense="food"
    elif expenseoftravel>expenseofshopping and expenseoftravel > expenseoffood:
        maxexpense="travel"
    elif expenseofshopping > expenseoftravel and expenseofshopping > expenseoffood:
        maxexpense="shopping"

    else:
        maxexpense=("some expenses are seems to be equal, so there is no highest expense.")

    return maxexpense
def percentage (expenseoffood,expenseoftravel,expenseofshopping):
    percentageoffood =(expenseoffood/total(expenseoffood,expenseoftravel,expenseofshopping))*100
    percentageoftravel =(expenseoftravel/total(expenseoffood,expenseoftravel,expenseofshopping))*100
    percentageofshopping =(expenseofshopping/total(expenseoffood,expenseoftravel,expenseofshopping))*100
    return percentageoffood,percentageoftravel,percentageofshopping
output=("")
while(output!="quit"):
    output=input("Enter your choice: ")
    if(output=="total"):
        print("total expense =",total(expenseoffood,expenseoftravel,expenseofshopping))
    elif(output=="highestexpense"):
        print("highest expense spend on =",highestexpense(expenseoffood,expenseoftravel,expenseofshopping))
    elif (output=="percentage"):
        print("percentage of each category of spending",percentage(expenseoffood,expenseoftravel,expenseofshopping))

    elif(output=="quit"):
        break
    else:
        print("system cant understand the command now.")