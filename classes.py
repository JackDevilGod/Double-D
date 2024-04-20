class Character:
    def __init__(self, name, speed):
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

        print("--".join(print_list))

    def next_round(self):
        self._front += 1

        if self._front >= len(self._timeline):
            self._front -= len(self._timeline)

        while self._timeline[self._front + 1].status() is False:
            self._front += 1

            if self._front >= len(self._timeline):
                self._front -= len(self._timeline)

    def remove(self):
        self.list_characters()

        character: int = int(input("character number to be removed\n"))

        if character < self._front:
            self._front -= 1

        self._timeline.pop(character)

    def stun(self):
        self.list_characters()

        character: int = int(input("character number to be removed\n"))

        self._timeline[character].deactivate(int(input("stun for how many turns")))


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


def main():
    return


if __name__ == "__main__":
    main()
