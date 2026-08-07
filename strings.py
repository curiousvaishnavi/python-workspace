#String Indexing

a = "Hello Buddy!"

print(a[4])


#String Slicing

print(a[0:5:1])

print(a[ : : ] )


# Note : Strings are Immutable in nature.


#Formatted Strings

name = "Bheem"

print(f"My name is {name}.")


"""Escape Sequences
   1) \ n :- Next Line
   2) \t :- For tab (5 Spaces)
   3) \b :- For Backspace"""

print("Welcome \nback")
print("Welcome \tback")
print("Welcome\b back")

#Raw String

print(r"Let's\n Go!")


"""Type Coonversions
   1) int()
   2) float()
   3) str()
   4) bool()"""

a = "23"

print(type(int(a)))
 # Note: Falsy values are 0,0.0,False,"",[],(),{} 

#Input Statement
#Note: Input bydefault type is String.


name = input("Tell me your name?")
print(name)
