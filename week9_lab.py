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