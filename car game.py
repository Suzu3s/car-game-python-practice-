
command = ""
started = False   # we used this boolean expression to set the conditions as already stopped and already started
while True:
    command = input("Give the command\n >").lower()
    if command.lower() == "help":
        print("start - to start the car"
          "\nstop - to stop the car"
          "\nquit - to exit ")
    elif command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started....Ready to go!")

    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "quit":
     break

    else:
      print("I don't understand that")