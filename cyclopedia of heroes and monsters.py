def main():
    # add players and enemies to data files.
    section: str | None = None
    action: str | None = None

    text_selected: str = "selected:"
    action_list: str = "add, remove, edit, return"

    while True:
        match section:
            case None:
                while section != "heroes" and section != "monsters":
                    print(text_selected + str(section))
                    section = input("heroes or monsters\n").lower()

            case "heroes" | "1":
                with open("players data.txt", "r") as player_sheet:
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
                pass

            case "remove" | "2":
                pass

            case "edit" | "3":
                pass

            case "return" | "4":
                section = None


def add_entity():
    with open("players data.txt", "w", newline="") as player_data_file:
        player_name: str = input("player name or exit\n")

        while player_name != "exit":
            speed: str = input("input speed\n")

            while speed.isnumeric() is False:
                speed: str = input("input speed\n")

            player_data_file.writelines(player_name + "," + speed + "\n")

            player_name = input("player name or exit\n")


if __name__ == "__main__":
    main()
