for i in range(int(input())):
    s=input()
    list= []
    for j in s:
        if j =='B' and len(list) > 0:
            list.pop()
        else:
            list.append(j)
    print(len(list))