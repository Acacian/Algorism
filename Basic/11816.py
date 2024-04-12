num = str(input())
tenarr = 0

if num[0] == '0' and num[1] == 'x': #16진수
    for i in range(2,len(num)):
        tn = 0

        if num[i] == 'a':
            tn = 10
        elif num[i] == 'b':
            tn = 11
        elif num[i] == 'c':
            tn = 12
        elif num[i] == 'd':
            tn = 13
        elif num[i] == 'e':
            tn = 14
        elif num[i] == 'f':
            tn = 15
        else:
            tn = int(num[i])

        tn = tn * (16 ** (len(num) - (i+1)))
        if (tn >= 1):
            tenarr += tn
    
    print(tenarr)
        
elif num[0] == '0' and num[1] != 'x': #8진수
    for i in range(1,len(num)):

        tn = int(num[i]) * (8 ** (len(num) - (i+1)))
        if (tn >= 1):
            tenarr += tn
            
    print(tenarr)

elif num[0] != '0':
    tenarr = int(num)
    print(tenarr)
else:
    tenarr = int(num)
    print(tenarr)
