def listFunc(a, b):
    return list(range(a, b + 1)) #Create list of ints from 1 to 5, Haskell equivalent [1..5]

def applicatorFunc(inpFunc, s, a, b):
    if s=='s':
        return sum(inpFunc(a, b))
    else:
        return sum(inpFunc(a, b))/(b-a)

print(applicatorFunc(listFunc, 'a', 1, 10))