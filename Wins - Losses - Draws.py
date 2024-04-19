import random

wins = 0
lose = 0
draws = 0

wins2 = 0
lose2 = 0
draws2 = 0

l = 1
while l < 1001:
    rps = [1, 2, 3]
    computer1 = random.randint(0,2)
    computer2 = random.randint(0,2)

    if computer1 == computer2:
        draws += 1
    elif computer1 == 1 and  computer2 == 3 or computer1 == 2 and computer2 == 1 or computer1 == 3 and computer2 == 2:
        wins += 1
    else:
        lose += 1

    if computer1 == computer2:
        draws2 += 1
    elif computer1 == 1 and  computer2 == 3 or computer1 == 2 and computer2 == 1 or computer1 == 3 and computer2 == 2:
        lose2 += 1
    else:
        wins2 += 1

    l += 1
if l == 1001:
    a = round((wins / 1000) * 100)
    b = round((lose / 1000) * 100)
    c = round((draws / 1000) * 100)
    d = round((wins2 / 1000) * 100)
    e = round((lose2 / 1000) * 100)
    f = round((draws2 / 1000) * 100)

    print("Computer #: wins(%)-lose(%)-draws(%)")
    print("Computer 1: " + str(wins) + "(" + str(a) + "%)-" + str(lose) + "(" + str(b) + "%)-" + str(draws) + "(" + str(c) + "%)")
    print("Computer 2: " + str(wins2) + "(" + str(d) + "%)-" + str(lose2) + "(" + str(e) + "%)-" + str(draws) + "(" + str(f) + "%)")