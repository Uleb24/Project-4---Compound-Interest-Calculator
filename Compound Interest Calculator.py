# Project 4 - Compound Interest Calculator

principal = 0 
rate = 0
time = 0 

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Your principal amount can't be negative !")
    else: 
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Your interest rate can't be negative !")
    else:
        break

while True:
    time = float(input("Enter the time (in years): "))
    if time < 0:
        print("Negative years don't exist !")
    else:
        break
        
total = principal * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")