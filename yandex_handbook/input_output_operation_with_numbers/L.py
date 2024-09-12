x = str(input())
z = str(input())
print(f"{(int(int(z) / 100 % 10) + int(int(x) / 100 % 10)) % 10}" +
      f"{(int(int(z) / 10 % 10) + int(int(x) / 10 % 10)) % 10}" +
      f"{(int(int(z) % 10) + int(int(x) % 10)) % 10}")
