import random

# Writing a programing task which Guess a random number.

n = random.randint(0,100)
appreciation = "?"
while True:
    var = input("Entrez un nombre")
    var = int(var)
    if var < n :
        appreciation = "Trop bas"
        print(var, appreciation)

    else :
        appreciation = "Trop haut"
        print(var, appreciation)
    if var == n:
        appreciation = "bravo !"
        print(var, appreciation)
        break