#problem 1

def isogram(word):
    letter_count = {}
    for letter in word:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            return False
            break
    return True


print(isogram("word"))


#problem 2

def unique(numbers):
    number_count = {}
    for number in numbers:
        if number not in number_count:
            number_count[number] = 1
        else:
            number_count[number] += 1
    for item in number_count:
        if number_count[item] == 1:
            return item
        else:
            continue

number_list = [1,2,2,3,3,4,4]
print(unique(number_list))


#problem 4

def just_name(names):
    name_list = []
    for key in names:
        name_list.append(key)
    return name_list

namesdict = {"Emma": 12345, "Bob": 67890}
print(just_name(namesdict))


#problem 5

def find_oldest(students):
    ages = []
    for name in students:
        ages.append(students[name])
    oldest = max(ages)
    for key, value in students.items():
        if value == oldest:
            return key


student_dict = {"Emma": 23, "Bob": 72, "Mildred": 86}
print(find_oldest(student_dict))


#problem 6

def letter_count(word):
    letter_ct_dict = {}
    for letter in word:
        if letter not in letter_ct_dict:
            letter_ct_dict[letter] = 1
        else:
            letter_ct_dict[letter] += 1
    return letter_ct_dict

print(letter_count("strings"))


#problem 7

def min_grade(exams):
    grades = []
    for subject in exams:
        grades.append(exams[subject])
    lowest_grade = min(grades)
    for key, value in exams.items():
        if value == lowest_grade:
            return key

exam_dict = {"Math": 23, "Science": 72, "History": 86}
print(min_grade(exam_dict))


#problem 8

def find_youngest(people):
    ages = []
    for name in people:
        ages.append(people[name])
    youngest = min(ages)
    for key, value in people.items():
        if value == youngest:
            return key


student_dict = {"Emma": 23, "Bob": 72, "Mildred": 86}
print(find_youngest(student_dict))


#hamming

def hamming(str1,str2):
    count = 0
    index = 0
    for letter in str1:
        if str1[index] != str2[index]:
            count += 1
            index += 1
        else:
            index += 1
    return count

print(hamming("abcde","bcdef"))


#problem 9

receipt = {"Chicken Nuggets" : 12, "Burger" : 10, "Grilled Cheese" : 8}
price = 0

for item in receipt:
    price += receipt[item]

print(price)


#problem 10

menu = {"Burger" : 10, "Fries" : 4, "Soda": 3}

for item in menu:
    print(f"{item} cost {menu[item]}")


#problem 11

def duplicates(elements):
    dupe_counts = {}
    for item in elements:
        if item not in dupe_counts:
            dupe_counts[item] = 1
        else:
            dupe_counts[item] += 1
    return dupe_counts

animals = ["dog", "cat", "cat", "cow", "cow", "cow"]
print(duplicates(animals))


#problem 12

def affordable(store, wallet):
    afford_items = []
    for item in store:
        if store[item] <= wallet:
            afford_items.append(item)
    return afford_items

store = {"Water": 1, "Bread": 3, "TV": 1000}
print(affordable(store, 300))


#problem 13

def total(sales):
    total_sales = []
    for item in sales:
        total_sales.append(sales[item])
    return sum(total_sales)

sales = {"Laptop": 5, "Phone": 10, "Tablet": 3}
print(total(sales))


#problem 14

def high_salary(salaries,limit):
    employees = []
    for name in salaries:
        if salaries[name] >= limit:
            employees.append(name)
    return employees

salaries = {"Emma": 10000, "Bob": 20000, "Mildred": 30000}
print(high_salary(salaries, 15000))


#problem 15

def donations(donors):
    total_donations = []
    for name in donors:
        total_donations.append(donors[name])
    return sum(total_donations)

donors = {"Emma": 5, "Bob": 10, "Mildred": 3}
print(donations(donors))


#problem 16

def calories(fruits):
    total_calories = []
    for fruit in fruits:
        total_calories.append(fruits[fruit])
    return sum(total_calories)

fruits = {"Apple": 100, "Banana": 250, "Peach": 173}
print(calories(fruits))


#problem 17

def cost(ingredients):
    total_cost = []
    for item in ingredients:
        total_cost.append(ingredients[item])
    return sum(total_cost)

ingredients = {"Flour": 5, "Eggs": 8, "Sugar": 3}
print(cost(ingredients))


#problem 18

def majority_element(nums):
    element_count = {}
    for number in nums:
        if number not in element_count:
            element_count[number] = 1
        else:
            element_count[number] += 1
    counts = []
    for element in element_count:
        counts.append(element_count[element])
        if element_count[element] == max(counts):
            majority = element
    return majority
        
numbers = [1,1,2,2,2,3,3,3,3,3,3,3,3,3,4,5,6]
print(majority_element(numbers))

