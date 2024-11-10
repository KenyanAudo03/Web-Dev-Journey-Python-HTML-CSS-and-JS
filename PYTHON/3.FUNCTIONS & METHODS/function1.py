def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

print(addition(1, 3))
print(subtraction(5, 2))
print(multiplication(4, 2))
print(division(10, 2))

name = input("Enter Your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
def profile(name, age, gender):
  return f"Your name is {name}, You are {age} and you are a {gender}."

print(profile(name, age, gender))


def profile(name, age, gender):
  return f"Your name is {name}, You are {age} and you are a {gender}."

print(profile(name, age, gender))


def profile(name,age):
  def greeting(hello):
    print("hello {name}.you are {age} years old")
    return f"{hello}{name}"
  return greeting("Goodnight")

name = input("what's your name? ")
age = int(input("what's your age?" ))
print(profile(name, age))