first = 15
second = 156
third = 156
if first == (second and third):
    print(3)
elif first == (second or third) or third == second:
    print(2)
elif first != (second and third) and second != third:
    print(0)
first2 = 122
second2 = 14
third2 = 453
if first2 == (second2 and third2):
    print(3)
elif first2 == (second2 or third2) or third2 == second2:
    print(2)
elif first2 != (second2 and third2) and second2 != third2:
    print(0)