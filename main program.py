from classes import *


def main():
    # TODO add function of saving player data to a separate file and read from it.

    timeline: Timeline = Timeline()

    # fill the list
    character_name: str = input("name of entity\n")

    while character_name != "":
        timeline.add(Character(character_name, float(input("speed\n"))))

        character_name: str = input("name of entity\n")

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
