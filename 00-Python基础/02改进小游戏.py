import random

print("---------My Games2-----------")
myint = random.randint(1,1000)
chances = 10
while chances:
    temp = input("请猜我心里的数字,您还有"+str(chances)+"次机会\n")
    guess = int(temp)
    if guess == myint:
        print("√正确,您猜对了")
        break
    else:
        if guess < myint:
            print("×错误,猜测数字小于实际\n")
        else:
            print("×错误,猜测数字大于实际\n")
    chances = chances - 1
print("游戏结束,正确答案是"+str(myint))

