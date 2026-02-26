import sys

# Lecture des paramètres
nbr1 = float(sys.argv[1])
op = sys.argv[2]
nbr2 = float(sys.argv[3])

def calculatrice(nbr1, op, nbr2):
    if op == '+' :
        return nbr1 + nbr2
    elif op == '-' :
        return nbr1 - nbr2
    elif op == '*' :
        return nbr1 * nbr2
    elif op == '/' :
        return nbr1 / nbr2
    return None

print(calculatrice(nbr1,op,nbr2))