def highway_directions(highway_num):
    if 1 <= highway_num <= 99:
        if highway_num % 2 == 0:
            return f"I-{highway_num} runs east/west"
        else:
            return f"I-{highway_num} runs north/south"
    elif 100 <= highway_num <= 999:
        if highway_num % 100 != 0:
            if highway_num % 2 == 0:
                return f"I-{highway_num} runs east/west"
            else:
                return f"I-{highway_num} runs north/south"
        else:
            return f"I-{highway_num} is an invalid highway"
    else:
        return f"I-{highway_num} is an invalid highway"

print(highway_directions(5))
print(highway_directions(82))
print(highway_directions(200))
print(highway_directions(353))

#blackjack problem redo
def blackjack(cards):
    score = 0
    for item in cards:
        if type(item) != str:
            if item < 7:
                score += 1
            elif item >= 7 and item <= 9:
                score += 0
        else:
            score -= 1
    return score

print(blackjack([2,3,4,5,6,"a",7]))

#problem 1

import random
def coin_toss(guess):
    possibilities = ["Heads", "Tails"]
    side = random.choice(possibilities)
    if guess == side:
        return True
    else:
        return False
    
print(coin_toss("Tails"))


#problem 4

def rock_paper_scissors(player1, player2):
    if player1 == player2:
        return "Draw"
    

#problem 7

def ascending(num1, num2 = 5, num3 = 25):
    a, b, c = num1, num2, num3
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return [a,b,c]

print(ascending(1,2,3))

#problem 15

def negative(number):
    if number < 0:
        return True
    else:
        return False

def odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

def negative_odd(numbers):
    neg_odd = []
    for item in numbers:
        if odd(item) and negative(item):
            neg_odd.append(item)
    return neg_odd

print(negative_odd([-3,4,-4,6,7,-7,-9,-10,-11]))

