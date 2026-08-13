#Left-shift in list

a = [10,20,30,40,50]

for i in range(len(a)-1):
    a[i],a[i+1]=a[i+1],a[i]

print(a)



#Reverse List
a = [10,20,30,40,50]
b = len(a)-1

for i in range(len(a)//2):
    a[i],a[b] = a[b],a[i]
    b -= 1

print(a)



#Linear Search
a = [1,2,4,3,45,34]
n = int(input("Enter element to search\n"))
for i in range(len(a)):
    if a[i]==n:
        print("Yes,It's present in the list!")
        break
else:
    print("Element not present in the list")




#Binary Search --applies only on sorted list


a = [12,14,24,56,57,89]
n = int(input("Enter number to search\n"))

start = 0
end = len(a)-1
mid = (start+end)//2

while start<=end:
    if a[mid]==n:
        print(f"Element found at index {mid}")
        break
    elif a[mid]<n:
        start = mid+1
        mid = (start+end)//2
    elif a[mid]<n:
        end = mid-1
        mid = (start+end)//2
    else:
        print("Sorry,You're element is not present in the list")
        break



#Bubble sort --Sorting elements by swapping the adjacent element

a = [1,2,3,88,54,35,64,75]
for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]

print(a)


#Selection sort -- Finding smallest element in the list and place it on it's appropriate position

a = [23,45,36,2,5,7,8]

for i in range(len(a)-1):
    j = i+1
    min = i
    for k in range(j,len(a)):
        if a[k]< a[min]:
            min = k

    a[i],a[min] = a[min],a[i]

print(a)