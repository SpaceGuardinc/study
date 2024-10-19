inp = input()

res = ''
for i in range(len(inp) - 1, -1, -1):
    res += inp[i]

if str(inp) == str(res):
    print("YES")
else:
    print("NO")
