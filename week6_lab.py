def skip_letter(yourwords):
    letters = []
    index = 0
    for letter in yourwords:
        if index <= len(yourwords):
            letter = yourwords[index]
            letters.append(letter)
            index += 2
        else:
            break
    return letters

print(skip_letter("counterattack"))


def even_numbers(small, large):
    numbers = []
    for number in range(small, large):
        if number % 2 == 0:
            numbers.append(number)
        else:
            continue
    return numbers

print(even_numbers(0,10))


def hailstone(n):
    hail_list = [n]
    while n > 1:
        if n % 2 == 0:
            n /= 2
            hail_list.append(n)
        else:
            n = n * 3 + 1
            hail_list.append(n)
    return hail_list

print(hailstone(25))


def factors(n):
    factor = []
    for number in range(1, n + 1):
        if n % number == 0:
            factor.append(number)
        else:
            continue
    return factor

print(factors(12))


def blackjack(cards):
    cardslist = []
    for item in cards:
        if type(item) != str:
            if (item >= 2) and (item <= 6):
                cardslist.append(1)
            elif (item >= 7) and (item <= 9):
                cardslist.append(0)
            else:
                cardslist.append(-1)
        else:
            cardslist.append(-1)
    score = sum(cardslist)
    return score

x = [2, 3, 4, 5, 6,"a"]

print(blackjack(x))


def acronym(string, list):
    liststring = ""
    for item in list:
        if item == "":
            liststring += "-"
        else:
            liststring += item[0]
    if liststring == string:
        return True
    else:
        return False
    
print(acronym("abc", ["alice", "bob", "charlie"]))