print("Welcome to our Car Game, enter help to get the commands")
is_started = False
is_stopped = False
while True:
    command = input("Enter a command >> ").lower()
    
    if command == "help":
        print("""
1. help - Get the commands
2. quit - Quit the Game
4. start - Start the Car
3. stop - Stop the Car
""")
    if command == "quit":
        print("You have quitted the game, goodbye!")
        break
    elif command == "start":
        if is_started:
            print("You have already started the Car")
        else:
            print("You have started the Car!")
            is_started = True
            is_stopped = False
            
    elif command == "stop":
        if is_stopped:
            print("You have already stopped the Car")
        else:
            print("Car stopped!")
            is_stopped = True
            is_started = False

