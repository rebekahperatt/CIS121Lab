#problem 1
'''
my_var = float(input("Input a number: "))

if my_var % 2 == 1:
    if my_var ** 3 !=27:   #assignment 1: if statement activated when my_var is any odd number that is not 3.
        my_var = my_var + 4     #range 
    else:                  #assignment 2: else statement activated when my_var = 3.
        my_var /= 1.5           #
else:
    if my_var <= 10:       #assignment 3: if statement activated when my_var is any even number less than or equal to 10.
        my_var *= 2             #
    else:                  #assignment 4: else statement activated when my_var is any even number greater than 10.
        my_var -= 2             #

print(my_var)

#problem 2
# a will test every block of code, while b will stop once one block is executed.

#problem 3
light_color = input("What is the color of the light? ")
if light_color == "Yellow" or "yellow":
    print("Yield.")
elif light_color == "Red" or "red":
    print("Stop.")
elif light_color == "Green" or "green":
    print("Go.")
else:
    print("Error.")
'''
#challenge problem

income = float(input("Yearly income in whole dollars: "))
marital_status = input("Are you married or single? Type M for married and S for single. ")

if marital_status == "M" or marital_status == "m":
    if (income >= 0) and (income <= 22000):
        tax = f"${income * 0.1}"
    elif (income >= 22001) and (income <= 89450):
        tax = f"${2200 + (income - 22000) * 0.12}"
    elif (income >= 89451) and (income <= 190750):
        tax = f"${2200 + 67450 * 0.12 + (income - 89450) * 0.22}"
    else:
        tax = "Wrong number entered."
elif marital_status == "S" or marital_status == "s":
    if (income >= 0) and (income <= 11000):
        tax = f"${income * 0.1}"
    elif (income >= 11001) and (income <= 44725):
        tax = f"${1100 + (income - 11000) * 0.12}"
    elif (income >= 44726) and (income <= 95375):
        tax = f"${1100 + 33725 * 0.12 + (income - 44725) * 0.22}"
    else:
        tax = "Wrong number entered."
else:
    print("Wrong status entered.")
    tax = "Wrong status entered."

print(f"Tax owed: {tax}")