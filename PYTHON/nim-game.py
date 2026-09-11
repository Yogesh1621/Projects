import random
n=int(input("Enter the initial number of stones: "))
x=n
while x>0:
    y=int(input("Your Move: "))
    z=random.randint(1,3)
    if 1<=y<=3 and y<=x:
        x=x-y
        if x==0:
            print("Win")
            break
        print("Remaining:", x)
        print("Computer's Move:", z)
        if z<=x:
            x=x-z
            if x==0:
                print("Lose")
                break
            print("Remaining:", x)