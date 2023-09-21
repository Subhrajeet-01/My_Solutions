for _ in range(int(input())):
    s = input()
    if s=="abc" or s=="acb" or s == "bac" or s == "cba":
        print("YES")
    else:
        print("NO")