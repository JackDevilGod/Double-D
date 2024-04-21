import os.path

from classes import *
import csv


def main():
    timeline: Timeline = Timeline()

    # fill the list with players
    current_directory = os.path.dirname(__file__)
    with open("../player data.csv", "r") as player_data_file:
        list_player_data = csv.reader(player_data_file)
        for player_data in list_player_data:
            timeline.add(Character(player_data[0], float(player_data[1])))

    # fill the list with enemies
    character_name: str = input("name of enemy\n")

    while character_name != "":
        timeline.add(Character(character_name, float(input("speed\n"))))

        character_name: str = input("name of enemy\n")

    actions: str = "next, remove, stun" + "\n"

    while True:
        timeline.print()

        action = input(actions).lower()

        while action != "next":
            if action == "remove":
                timeline.remove()
            elif action == "stun":
                timeline.stun()

            action = input(actions).lower()

        timeline.next_round()


if __name__ == "__main__":
    main()
