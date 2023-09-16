#To print all positive numbers in a range

list1 = [12, -7, 5, 64, -14]
for i in list1:
    if i<0:
        list1.remove(i)
print("The positive numbers are :",list1)