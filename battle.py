def main():
    timeline: Timeline = Timeline()

    # fill the list with players
    with open("player data.csv", "r") as player_data_file:
        list_player_data = player_data_file.readlines()

        for player_data in list_player_data:
            player_data_spliced = player_data.split(",")

            timeline.add(Character(player_data_spliced[0], float(player_data_spliced[1])))

    # fill the list with enemies
    character_name: str = input("name of enemy\n")

    while character_name != "":
        timeline.add(Character(character_name, float(input("speed\n"))))

        character_name: str = input("name of enemy\n")

    actions: str = "next, remove, stun, exit" + "\n"

    while True:
        timeline.print()

        action = input(actions).lower()

        while action != "next":
            match action:
                case "remove":
                    timeline.remove()
                case "stun":
                    timeline.stun()
                case "exit":
                    return

            action = input(actions).lower()

        timeline.next_round()


class Character:
    def __init__(self, name: str, speed: float | int):
        self.name: str = name
        self.speed: float | int = speed
        # active or not
        self._status: bool = True
        self._turns: int = 0
        self._effect_time: int = 0

    def status(self):
        return self._status

    def status_check(self):
        if self._status is False:
            self._turns += 1

        if self._turns == self._effect_time:
            self.activate()

        return self._status

    def activate(self):
        self._status = True
        self._turns = 0

    def deactivate(self, effect_time: int):
        self._status = False
        self._effect_time = effect_time

    def turns(self):
        return self._turns

    def __lt__(self, other):
        return self.speed < other.speed


class Timeline:
    def __init__(self):
        self._timeline: list[Character] = []
        self._front = 0

    def list_characters(self):
        temp = []
        for index in range(len(self._timeline)):
            temp.append(str(index) + "." + self._timeline[index].name)

        print(" ".join(temp))

    def add(self, character: Character):
        self._timeline.append(character)
        self._timeline = mergesort_character_list(self._timeline)

    def print(self):
        print_list: list[str] = []

        if self._front == 0:
            for character in self._timeline:
                if character.status_check():
                    print_list.append(character.name)
        else:
            for part in [self._timeline[self._front:], self._timeline[:self._front]]:
                for character in part:
                    if character.status_check():
                        print_list.append(character.name)

        print(" -- ".join(print_list))

    def next_round(self):
        self._front += 1
        next_index = self._front + 1

        if self._front >= len(self._timeline):
            self._front -= len(self._timeline)
            next_index -= len(self._timeline)
        elif next_index >= len(self._timeline):
            next_index -= len(self._timeline)

        while self._timeline[next_index].status() is False:
            self._front += 1
            next_index += 1

            if self._front >= len(self._timeline):
                self._front -= len(self._timeline)
                next_index -= len(self._timeline)
            elif next_index >= len(self._timeline):
                next_index -= len(self._timeline)

    def remove(self):
        self.list_characters()

        character: int = int(input("character number to be removed\n"))

        if character < self._front:
            self._front -= 1

        self._timeline.pop(character)

    def stun(self):
        self.list_characters()

        character: int = int(input("character number to be removed\n"))

        stun_duration = input("stun for how many turns")

        while stun_duration.isnumeric() is False:
            stun_duration = input("stun for how many turns")

        self._timeline[character].deactivate(int(stun_duration))


def mergesort_character_list(lst: list[Character]):
    if len(lst) == 1:
        return lst
    else:
        sorted_list: list[Character] = []

        middle_point: int = len(lst)//2
        front_half: list[Character] = mergesort_character_list(lst[:middle_point])
        back_half: list[Character] = mergesort_character_list(lst[middle_point:])

        index_front_half: int = 0
        index_back_half: int = 0

        while index_front_half < len(front_half) and index_back_half < len(back_half):
            if front_half[index_front_half] > back_half[index_back_half]:
                sorted_list.append(front_half[index_front_half])
                index_front_half += 1
            else:
                sorted_list.append(back_half[index_back_half])
                index_back_half += 1

        if index_front_half < len(front_half):
            sorted_list += front_half[index_front_half:]
        elif index_back_half < len(back_half):
            sorted_list += back_half[index_back_half:]

        return sorted_list


if __name__ == "__main__":
    main()
