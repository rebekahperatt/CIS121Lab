
#problem 1

larger = float(input("Input a large number: "))
larger_original = str(larger)
smaller = float(input("Input a small number: "))
count = 0

while larger > smaller:
    if larger/2 >= smaller:
        larger = larger/2
        count += 1
    else:
        break

print(f"{larger_original} can be divided in half {count} times before it is smaller than {smaller}.")

#problem 2

user_word = input("Choose a word: ")
print(user_word[1::2])

#problem 3

for number in range (38,1051,2):
    print(number)

#problem 4

word = []

while True:
    letter = input("Input a letter or type done to exit: ")
    if letter != "done":
        word.append(letter)
    else:
        break

print(''.join(word))

#problem 5

sum_num = []
for number in range(51,518,2):
    sum_num.append(number)
print(sum(sum_num))

#problem 6

number_list = []
while True:
    user_number = float(input("Add a number or enter a negative to exit: "))
    if user_number > 0:
        number_list.append(user_number)
    elif user_number < 0:
        break

print(f"The sum of your numbers is : {sum(number_list)}")

#question 7

n = 25
n_list = []
while n != 1:
    if n % 2 == 0:
        n = n/2
        n_list.append(n)
    elif n % 2 == 1:
        n = n * 3 + 1
        n_list.append(n)

print(n_list)

#nested loops
'''
upper_bound = int(input("Upper bound: "))
proper_divs = []
for number in range(1,upper_bound):
    if upper_bound % number == 0:
        proper_divs.append(number)

sum_divisors = sum(proper_divs)

if sum_divisors == upper_bound:
    perfect_number = 1
elif sum_divisors > upper_bound:
'''