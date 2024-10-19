num = int(input())

divisor = 2
prime = True

if -1 <= num <= 1:
    prime = False
else:
    while divisor ** 2 <= num and prime is True:
        if num % divisor == 0:
            prime = False
        else:
            divisor = divisor + 1

if prime is True:
    print('YES')
else:
    print('NO')

# x = int(input())
#
# k = 0
#
# for i in range(1, x + 1):
#     if x % i == 0:
#         k = k + 1
#
# if k == 2:
#     print("YES")
# else:
#     print("NO")
