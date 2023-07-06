#lecture information function

#labaratory information function

#a function that analyzes the request
def analyzes():
    if intrest == 'laboratory':
        return "The laboratory is in room A203."
    elif intrest == 'lectures':
        return "The lecture hall is in room A112."

#main part of the program
intrest = input("What are you interested in? (stop - exit)")
while intrest != 'stop':
    print(analyzes())
    intrest = input("What are you interested in? (stop - exit)")

print('Goodbey!')