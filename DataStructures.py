#Inbuilt DataStructures

# 1)List
"""Note:
 -List is Mutable in nature
 a = [1,2,3,4,5,7]
    a[5] = 6
    print(a)
 -List have Heterogenous nature means we can store multiple datatypes at the same instance
 -List can store duplicate values also"""


# a)Deep-Copy

import copy
a = [1,2,3,4]
b = copy.deepcopy(a)

#Note: Now a and b both referred same memory location

#List Traversing (Method 1)

a = [1,2,3,4]

for i in a:
    print(i)


#List Traversing (Method 2)- Index based

a = [10,20,30,40]

for i in range(len(a)):
    print(a[i])

