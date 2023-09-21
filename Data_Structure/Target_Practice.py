t = int(input())
for _ in range(t):
    m = [list(input()) for _ in range(10)]
    p = 0
    for i in range(10):
        for j in range(10):
            if m[i][j] == 'X':
                res = min(i, j, 9 - i, 9 - j)
                p += (res + 1)

    print(p)






# for _ in range(int(input())):
#     res = 0
#     for i in range(10):
#         s = input()
#         c = s.count('X')
#         if c == 1:
#             x = s.index('X')
#             if i == 0 or i == 9 or x == 0 or x == 9:
#                 res += 1
#             elif i == 1 or i == 8 or x == 1 or x == 8:
#                 res += 2
#             elif i == 2 or i == 7 or x == 2 or x == 7:
#                 res += 3
#             elif i == 3 or i == 6 or x == 3 or x == 6:
#                 res += 4
#             else:
#                 res += 5
#         else:
#             for j in range(10):
#                 if i == 0 or i == 9 or x == 0 or x == 9:
#                     res += 1
#                 elif i == 1 or i == 8 or x == 1 or x == 8:
#                     res += 2
#                 elif i == 2 or i == 7 or x == 2 or x == 7:
#                     res += 3
#                 elif i == 3 or i == 6 or x == 3 or x == 6:
#                     res += 4
#                 else:
#                     res += 5
#     print(res)



