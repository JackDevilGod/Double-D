def main():
    # add players and enemies to data files.
    pass


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
