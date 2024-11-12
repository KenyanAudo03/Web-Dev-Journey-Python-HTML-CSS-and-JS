number = 0
while number < 5:
    print("Hello World!", number)
    number += 1


secret_number = 5
number_of_guesses = 0
remaining_attempts = 5
while number_of_guesses < 5:
    try:
        guess_number = int(input("Guess a number: "))
        remaining_attempts -= 1
        if guess_number == secret_number:
            print("You won 🎉!")
            break

        else:
            print("You are wrong 🎭!")

        number_of_guesses += 1

        print("You are remaining with", remaining_attempts, "🎯 attempts!")

    except:
        print("Use numbers only ❌.")
else:
    print("You are out of guesses ❗")
