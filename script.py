import os

lst1 = [8, 9, 3, 6, 1, 10]
lst1.reverse()
print(f"Reversed list is: {lst1}")

lst2 = [91, 67, 120, 34, 76, 54, 78, 87, 56, 64, 345]
lst2.sort()
print(f"Sorted list. {lst2}")

lst3 = []
lst3 = lst1.copy()
print(f"List 3 is: {lst3}")

index_value = lst2[2:6]
print("The index values are", index_value)
