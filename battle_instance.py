from classes import *


def battle():
    timeline: Timeline = Timeline()

    # fill the list with players
    with open("player data.csv", "r") as player_data_file:
        list_player_data = player_data_file.readlines()

        for player_data in list_player_data:
            player_data_spliced = player_data.split(",")

            timeline.add(Character(player_data_spliced[0], float(player_data_spliced[1])))

    # fill the list with enemies
    character_name: str = input("name of enemy\n")

    while character_name != "":
        timeline.add(Character(character_name, float(input("speed\n"))))

        character_name: str = input("name of enemy\n")

    actions: str = "next, remove, stun, exit" + "\n"

    while True:
        timeline.print()

        action = input(actions).lower()

        while action != "next":
            match action:
                case "remove":
                    timeline.remove()
                case "stun":
                    timeline.stun()
                case "exit":
                    return

            action = input(actions).lower()

        timeline.next_round()
