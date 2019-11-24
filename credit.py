# This program tests to see if the credit card number inputed by the user
# is a mastercard visa or american express
# Lucas Dahl

case = False
while case == False:
    try:
        credit = int(input("Number: "))
    except ValueError:
        case = False
    else:
        case = True
#AE 34 or 37 start 15 digit
#MC start 51 52 53 54 55 and 16 digit
#VI start 4 and 13 and 16 digit
count = int(credit)
# Digits is used to count how many digits are in the card number
digits = 0
# Divisor is used while checking the card as a placeholder to keep the number created
# when the digits are multiplied by 2 and get the remaineder do to Luhn's
# algorithm
# 1) Every other digit multiplied by 2 starting with second to last and add them all
# 2) Add the sum from 1 to the sum of all the other digits
# 3) If the modulus of the total is 0 it is a valid number
divisor = 0
#Loop to determine the amount of digits
while count != 0:
    digits = digits + 1
    count = int(count / 10)
# Initialize the list to break up the credit card numbers digits
creditlist = []
for i in range(0, digits):
    creditlist.append(0);
# Loop to get each individual digit using modulus
for i in range(0, digits):
    creditlist[i] = credit % 10
    credit = int(credit / 10)

total=0
# Test Case for VISA
if digits == 13:
    # Loop though all the digits
    for i in range(0, digits):
        # Checks if the digit number is even to do every other digit and adds them
        if i % 2 == 0:
            total = total + creditlist[0 + i]
        # Otherwise it multiplies the digit by 2, if less then 9 just multiplies by 2
        else:
            if 2 * creditlist[0 + i] < 9:
               total = total + 2 * creditlist[0 + i]
            # If it is greator then 9 it will need to be modulus checked to find the remainder values
            else:
                divisor = 2 * creditlist[0 + i]
                total = total + divisor % 10
                divisor = int(divisor / 10)
                total = total + divisor
    # If its mod is 0 and the first digit is 4, (It loads to the list in reverse order so last digit in list)
    if total % 10 == 0 and creditlist[digits - 1] == 4:
        #If it passes visa test
        print("VISA")
    else:
        #it failed visa test
        print("INVALID")

#test for Mastercard
elif digits == 16:
    # Likewise explination for this loop as the loop above
    for i in range(0, digits):
        if i % 2 == 0:
            total = total + creditlist[0 + i]
        else:
            if 2 * creditlist[0 + i] < 9:
                total = total + 2 * creditlist[0 + i]
            else:
                divisor = 2 * creditlist[0 + i]
                total = total + divisor % 10
                divisor = int(divisor / 10)
                total = total + divisor
    if total % 10 == 0 and creditlist[digits - 1] == 4:
        #passed visa not mastercard
        print("VISA")
    elif total % 10 == 0 and creditlist[digits - 1] == 5 and (creditlist[digits - 2] == 1 or creditlist[digits - 2] == 2 or creditlist[digits - 2] == 3 or creditlist[digits - 2] == 4 or creditlist[digits - 2] == 5):
        #passed mastercard
        print("MASTERCARD\n")
    else:
        print("INVALID\n")
        #failed both cases

elif digits == 15:
    # Likewise explination for this loop as the first loop above
    for i in range(0, digits):
        if i % 2 == 0:
            total = total + creditlist[0 + i]
        else:
            if 2 * creditlist[0 + i] < 9:
                total = int(total + 2 * creditlist[0 + i])
            else:
                divisor = int(2 * creditlist[0 + i])
                total = total + divisor % 10
                divisor = int(divisor / 10)
                total = total + divisor
    if total % 10 == 0 and creditlist[digits - 1] == 3 and (creditlist[digits - 2] == 4 or creditlist[digits - 2] == 7):
        print("AMEX")
        #last test passed american express
    else:
        print("INVALID")

else:
    print("INVALID")