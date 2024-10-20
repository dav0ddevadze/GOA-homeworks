
def divide_numbers(a, b):
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero!")


divide_numbers(10, 2)  

def greet(name):
    print(f"Hello, {name}! Welcome!")


greet("david")  

def multiplyby(num):
    print(num * 5)


multiplyby(4)  

def user():
    age = input("Enter your age: ")
    ename = input("Enter your name: ")
    print(f"Your name is {ename} and your age is {age}")

user()
