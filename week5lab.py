#strings
#problem 1
def reverse_string(word):
    wordnew = str(word)[::-1]
    return wordnew

print(reverse_string("hello"))

#problem 2
def fever_det(string):
    temp = float(string[0:-1])
    if string[-1] == "C":
        if temp > 37:
            fever = True
        else:
            fever = False
    elif string[-1] == "F":
        if temp > 98.6:
            fever = True
        else:
            fever = False
    return fever

print(fever_det("38C"))

#harry potter problem

def hp_coins(knut):
    galleon = knut//493
    sickle = (knut - (galleon*493))//29
    knuts = knut - sickle*29
    output = ""
    if galleon > 0:
        output += f"{galleon} galleons, "
    if sickle > 0:
        output += f"{sickle} sickles, "
    if knuts > 0:
        output += f"and {knuts} knuts."
    return output

print(hp_coins(32))

#problem 4

#string1 = input("word: ")
#string2 = input("word: ")

def hamming(str1, str2):
    count = 0
    while str1 != "" and str2 != "":
        if str1[-1] == str2[-1]:
            str1 = str1[0:-1]
            str2 = str2[0:-1]
        else:
            str1 = str1[0:-1]
            str2 = str2[0:-1]
            count += 1
    return count

print(hamming("abcdef", "abshdef"))

#leetcode

input_string = "This is a sample string"
first_letters = ""

for word in input_string.split():
    first_letters += word[0]

print(first_letters)