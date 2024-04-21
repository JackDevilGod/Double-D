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
                case "add":
                    # TODO add an adding function

            for player in player_sheet:
                print(" ".join(player))


def add_player():
    pass


if __name__ == "__main__":
    main()
