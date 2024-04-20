from classes import *
from function import *


def main():
    characters: list[Character] = []

    # fill the list
    character_name: str = input("name of entity\n")

    while character_name != "":
        characters.append(Character(character_name, float(input("speed\n"))))

        character_name: str = input("name of entity\n")

    # sort the turn order and put into timeline
    timeline = Timeline(mergesort_character_list(characters))

    while True:
        timeline.print()

        action = input().lower()

        while action != "next":
            if action == "remove":
                timeline.remove()

            action = input().lower()

        timeline.next_round()


if __name__ == "__main__":
    main()
