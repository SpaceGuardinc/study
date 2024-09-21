
a = int(input())
b = int(input())
c = int(input())

if a < b + c and c < b + a and b < a + c:
    print("YES")
else:
    print("NO")
