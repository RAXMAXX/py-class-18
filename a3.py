lst = [10,23,42,4,8,45]
print("list :", lst)

sum = 0
for i in  lst:
     sum =sum + i

     avg = sum/ len(lst)

     print("sum = " ,sum)
     print("average =",avg)

     lst.sort()
     print("Smallest No:", lst[0])
     print("Largest No:", lst[-1])