from function import *


def main():
    timeline: Timeline = Timeline()

    # fill the list
    character_name: str = input("name of entity\n")

    while character_name != "":
        timeline.add(Character(character_name, float(input("speed\n"))))

        character_name: str = input("name of entity\n")

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
