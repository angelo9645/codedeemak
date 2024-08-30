num = input().split

if(len(num)>1):
    print("Too much input!")
else:
    num = int(num[0])
    for i in range(1,13):
        print(num ,"x",i,"=",num * i)    