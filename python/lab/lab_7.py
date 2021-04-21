# Chapter 7 Lab
room_list = []
bedroom1 = ["This is the first Bedroom.\nThere are rooms to the east and south.", None, 4, 0, None]
bedroom2 = ["This is the second Bedroom.\nThere are rooms to the north and east.", 3, 1, None, None]
south_hall = ["This is the South Hall.\nThere are rooms to the north and east and west.", 4, 2, 0, None]
north_hall = ["This is the North Hall.\nThere are rooms to the north and east and south and west.", 6, 5, 1, 3]
kitchen = ["This is the Kitchen.\nThere are rooms to the south and west.", None, None, 2, 4]
dining_room = ["This is the Dining Room.\nThere are rooms to the north and west.", 5, None, None, 1]
balcony = ["This is the Balcony.\nThere are rooms to the south.", None, None, 4, None]
room_list.append(bedroom2)
room_list.append(south_hall)
room_list.append(dining_room)
room_list.append(bedroom1)
room_list.append(north_hall)
room_list.append(kitchen)
room_list.append(balcony)

current_room = 0
done = False
while not done:
    print(room_list[current_room][0])
    print("")
    user_input = input("Where do you want to go?\n")
    if user_input == "n" or user_input == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way.\n")
        else:
            current_room = next_room
    elif user_input == "e" or user_input == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way.\n")
        else:
            current_room = next_room
    elif user_input == "s" or user_input == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way.\n")
        else:
            current_room = next_room
    elif user_input == "w" or user_input == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way.\n")
        else:
            current_room = next_room
    else:
        print("I don't understand what you typed.\n")
    
    stop = input("Do you want to stop? y/n\n")
    if stop == "y" or stop == "yes":
        done = True