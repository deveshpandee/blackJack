import random
import logo
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
list1=[]
list2=[]



def takeCard(lis):
    lis.append(random.choice(cards))
def clear(lis):
    lis=[]
    return lis
def result():
    print("\nYour cards",list1,"\nYour total:",sum(list1))
    print("\nComputer's card:",list2,"\nComputer's total:",sum(list2))
    if (sum(list1)<22 & sum(list2)<22):
        if sum(list1)>sum(list2):
            print("You won😄😄\n")
        elif sum(list2)>sum(list1):
            print("You lose😢😢\n")
        else:
            print("It was a draw🤝🤝\n")
    elif sum(list1)>21:
        print("\nYou went over 21.")
        print("You lose😢😢\n")
    elif sum(list2)>21:
        print("\nComputer went over 21.")
        print("You won😄😄\n")
    else:
        print("It was a draw🤝🤝\n")
    

def play():
    print("\033c", end="")
    print(logo.logo)
    takeCard(list1)
    takeCard(list1)
    takeCard(list2)
    takeCard(list2)
    k=1
    while k:
        print("Your cards:",list1)
        print("Your total:",sum(list1))
        print(f"\nComputer's card: [{list2[0]},X]")
        wish=int(input("\nEnter '1' to take more card or '0' to pass."))
        if wish==1:
            takeCard(list1)
            if sum(list1)>21:
                for i in list1:
                    if i==11:
                        list1[list1.index(i)]=1
            if sum(list1)>21:
                result()
                break
        elif wish==0:
            while True:
                if sum(list2)>=sum(list1):
                    result()
                    k=0
                    break
                if sum(list2)<sum(list1):
                    takeCard(list2)
                    print("Your cards:",list1)
                    print("Your total:",sum(list1))
                    print("Computer's card:",list2)
                elif sum(list2)>21:
                    result()
                    k=0
                    break
        else:
            print("Invalid Input")
            break