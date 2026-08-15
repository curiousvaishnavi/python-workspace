#Exception Handling

try:
    print(10/0)
except Exception as err:                        # Here, Exception----is Universal Catcher
    print("Sorry an error occurred!")
else:
    print("Everything is Ok!")
finally:
    print("You're Awesome!")



#Custom Exception Handling ------raise

try:
    age = int(input("Enter your age"))
    if age<18:
        raise Exception("Not Eligible!")
    print("Eligible!")
except Exception as err:
    print("Error is Occurred!",err)