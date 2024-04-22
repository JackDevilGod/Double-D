from battle_instance import *


def main():
    with open("player data.txt", "r") as player_sheet_file:
        player_sheet = player_sheet_file.readlines()

        for player in player_sheet:
            print(" ".join(player.split(",")))

    action_list: str = "add player, battle" + "\n"
    action: str = input(action_list).lower()

    while True:
        match action:
            case "battle":
                battle()
            case "add player":
                add_player()

        with open("player data.txt", "r") as player_sheet_file:
            player_sheet = player_sheet_file.readlines()

            for player in player_sheet:
                print(" ".join(player.split(",")))

        action: str = input(action_list).lower()


def add_player():
    with open("player data.txt", "w", newline="") as player_data_file:
        player_name: str = input("player name or exit\n")

        while player_name != "exit":
            speed: str = input("input speed\n")

            while speed.isnumeric() is False:
                speed: str = input("input speed\n")

            player_data_file.writelines(player_name + "," + speed + "\n")

            player_name = input("player name or exit\n")


if __name__ == "__main__":
    main()
