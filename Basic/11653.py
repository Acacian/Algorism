
num = int(input())

while(1):
    if num == 1:
        break
    elif num % 2 != 0 and num % 3 == 0:
        num = num / 3
        print(3)
    elif num % 2 == 0:
        num = num / 2
        print(2)
    else:
        for i in range(2,10000000):
            if num % i == 0:
                num = num / i
                print(i)
                break

