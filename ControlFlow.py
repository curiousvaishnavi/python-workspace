#1) if-else statement

# age = int(input("Enter your age :-"))

if age>=18:
    print("You can vote!")
else:
    print("Not eligible to vote!")


#2) Ternary Operator

print("You're grown up!") if age>=18 else print("You're kid!")

#3) if-elif ladder

if age == 18:
    print("You're grown up!")
elif age > 18:
    print("You're kid!")
else:
    print("You're Learning!!")

#4) for loop

num = range(5,51,5)

for i in num:
    print(i)
