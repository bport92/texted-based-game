inventory = []


def game():
    print("You are standing at a locked door and there is a key on the ground.")
    in_room = True

    while True == in_room:
        action = input("What do you do?: ").lower().strip()

        if action == "pick up key":
            print("You picked up the key and added it to your inventory")
            inventory.append("key")

        elif action == "open door" and "key" not in inventory:
            print("The door is locked")

        elif action == "open door" and "key" in inventory:
            print("The door opens")
            inventory.remove("key")
            in_room = False

        else:
            print("I do not understand")
    else:
        print("Congrats! you made it out!")


game()
