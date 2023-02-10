
def main():
    print("Welcome to tip calculator")

    totalBill = float(input("What was the total bill amount ?"))

    tipPercent = int(input("How much percent would you like to give tip ? "))

    peopleCount = int(input("How many people to split the bill ?"))

    individualShare = round(Calculate(totalBill,tipPercent,peopleCount),2)
    print("***********************************")
    print(f"  Each person should pay ${individualShare}")
    print("***********************************")

def Calculate(bill,tip,people):
    tipAsPercent = tip/100
    totalTipAmount = bill * tipAsPercent

    return (bill + totalTipAmount) / people


main()
