import random


def generaterandom(upper):
    r = random.randint(1, upper)
    return r


def main():
    run = True
    num1 = generaterandom(10)
    num2 = generaterandom(10)
    result = num1 * num2
    while run:
        ans = input("what is"+str(num1)+"x"+str(num2)+"= ?")
        if ans.isdigit():
            if int(ans) == result:
                print("correct !")
                run = False
            else:
                print("incorect ! try again.")

        else:
            print("answer must be a positive numberm, try again")
