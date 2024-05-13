"""
player:
<name>,<race>,<class>,<hit points>,<defence>,<speed>,<strength>,<dexterity>,<constitution>,<intelligence>,<wisdom>,<charisma>,<skills>,<description>
monster:
<name>,<hit points>,<defence>,<speed>,<strength>,<dexterity>,<constitution>,<intelligence>,<wisdom>,<charisma>,<skills>,<description>
"""
data_type_list: list[str] = ["<name>", "<race>", "<class>", "<hit points>", "<defence>", "<speed>", "<strength>",
                             "<dexterity>", "<constitution>", "<intelligence>", "<wisdom>", "<charisma>", "<description>", "<skills>"]


def main():
    # add players and enemies to data files.
    section: str | None = None
    action: str | None = None

    text_selected: str = "selected:"
    action_list: str = "add, remove, edit, view, return" + "\n"

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
                remove_entity(section)

            case "edit" | "3":
                pass

            case "view" | "4":
                pass

            case "return" | "5":
                section = None
                action = None


def add_entity(entity_type: str):
    with open(entity_type + " data.txt", "r") as sheet:
        data: list[str] = [_ for _ in sheet.readlines() if _ != "\n"]

    stats: list[str] = []

    with (open(entity_type + " data.txt", "w") as sheet):
        stat_list = data_type_list

        for index in range(len(stat_list)):
            temp_stat = input(stat_list[index] + "\n")

            while 2 < index < 12 and temp_stat.isnumeric() is False and entity_type == "heroes":
                temp_stat = input(stat_list[index] + "\n")

            if index < len(stat_list) - 1:
                stats.append(temp_stat)

            while index == len(stat_list) - 1 and temp_stat != "":
                skill_description = input("describe skill\n")
                stats.append(temp_stat + ":" + skill_description)

                temp_stat = input("<skill> or enter to stop")

        data.append(",".join(stats) + "\n")

        for line in data:
            sheet.write(line)


def remove_entity(entity_type: str):
    pass


if __name__ == "__main__":
    main()
