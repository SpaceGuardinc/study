nature1 = input()
nature2 = input()
nature3 = input()

if nature1 > nature2:
    nature1, nature2 = nature2, nature1
if nature1 > nature3:
    nature1, nature3 = nature3, nature1
if nature2 > nature3:
    nature2, nature3 = nature3, nature2

if 'зайка' in nature1:
    print(nature1, len(nature1))
elif 'зайка' in nature2:
    print(nature2, len(nature2))
elif 'зайка' in nature3:
    print(nature3, len(nature3))