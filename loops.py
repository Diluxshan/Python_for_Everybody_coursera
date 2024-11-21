x = 5

def basic_while():
    while x>0:
        print(x)
        x = x -1
    print("Done!")

def advance_while(x):
    while x>0:
        continue
        x=x-1
    print("Done2")

advance_while(x)