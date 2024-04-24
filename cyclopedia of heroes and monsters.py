"""
player:

monster:
<name>,<hit points>,<defence>,<speed>,<strength>,<dexterity>,<constitution>,<intelligence>,<wisdom>,<charisma>,<skills>
"""


def main():
    # add players and enemies to data files.
    section: str | None = None
    action: str | None = None

    text_selected: str = "selected:"
    action_list: str = "add, remove, edit, return" + "\n"

    while True:
        match section:
            case None:
                while section != "heroes" and section != "monsters":
                    print(text_selected + str(section))
                    section = input("heroes or monsters\n").lower()

            case "heroes" | "1":
                with open("heroes data.txt", "r") as player_sheet:
                    player_sheet = player_sheet.readlines()
                    print("-".join([_.split(",")[0] for _ in player_sheet]))

                action = input(action_list)

            case "monsters" | "2":
                with open("monsters data.txt", "r") as monster_sheet:
                    monster_sheet = monster_sheet.readlines()
                    print("-".join([_.split(",")[0] for _ in monster_sheet]))

                action = input(action_list)

        match action:
            case "add" | "1":
                add_entity(section)

            case "remove" | "2":
                pass

            case "edit" | "3":
                pass

            case "return" | "4":
                section = None


def add_entity(entity_type: str):
    with open(entity_type + " data.txt", "r") as sheet:
        data: list[str] = sheet.readlines()

    with open(entity_type + " data.txt", "w") as sheet:
        entity_name: str = input("name\n")

        for stat in []:
            pass


if __name__ == "__main__":
    main()
