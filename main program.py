from battle_instance import *


def main():
    with open("player data.csv", "r") as player_sheet_file:
        player_sheet = csv.reader(player_sheet_file)

        for player in player_sheet:
            print(" ".join(player))

        action_list: str = "add player, battle" + "\n"
        action: str = input(action_list).lower()

        while True:
            match action:
                case "battle":
                    battle()
                case "add player":
                    add_player()

            for player in player_sheet:
                print(" ".join(player))

            action: str = input(action_list).lower()


def add_player():
    with open("player data.csv", "w", newline="") as player_data_file:
        player_csv = csv.writer(player_data_file, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)

        player_name: str = input("player name or exit")

        while player_name != "exit":
            speed: str = input("input speed")

            while speed.isnumeric() is False:
                speed: str = input("input speed")

            player_csv.writerow([player_name, speed])

            player_name = input("player name or exit")


if __name__ == "__main__":
    main()
