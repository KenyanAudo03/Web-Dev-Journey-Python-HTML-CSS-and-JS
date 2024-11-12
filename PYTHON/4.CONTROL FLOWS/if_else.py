age = int(input("Enter your age: ").strip())


if age >= 13 and age <= 19:
    if age >= 18:
        print("You are a teenager and an adult...")
    else:
        print("You are a teenager")
elif age >= 18:
    print("Your are an adult...")
elif  age < 13 and age >= 0:
    print("Chop Rise...")
else:
    print("Invalid age!! Must be 0 and above.")