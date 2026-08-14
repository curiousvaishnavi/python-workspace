#Lambda expression --Short hand function


add = lambda a,b:a+b
print(add(13,12))


#map() ---function ko har ek element ke upar aaply karna ho to use karte hai

a = [1,2,3,4]

l =map(lambda x:x**2,a)
print(list(l))


#filter() -----filters items from the list on the basis of the condition
a = [1,2,3,4,5]
l = filter(lambda x: x%2==0,a)
print(list(l))


#zip() ----- combine multiple iterables into the pairs of elements

name = ["Karan","Rahul"]
age = [13,16]

mixed = zip(name,age)
print(dict(list(mixed)))