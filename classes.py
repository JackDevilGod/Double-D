class Character:
    def __init__(self, name, speed):
        self.name: str = name
        self.speed: float | int = speed
        self._status: bool = True

    def __lt__(self, other):
        return self.speed < other.speed


class Timeline:
    def __init__(self):
        self._timeline: list[Character] = []
        self._front = 0

    def add(self, character: Character):
        self._timeline.append(character)
        self._timeline = mergesort_character_list(self._timeline)

    def print(self):
        print_list: list[str] = []

        if self._front == 0:
            for character in self._timeline:
                print_list.append(character.name)
        else:
            for character in self._timeline[self._front:]:
                print_list.append(character.name)

            for character in self._timeline[:self._front]:
                print_list.append(character.name)

        print("--".join(print_list))

    def next_round(self):
        self._front += 1

        if self._front >= len(self._timeline):
            self._front -= len(self._timeline)

    def remove(self):
        temp = []
        for index in range(len(self._timeline)):
            temp.append(str(index) + "." + self._timeline[index].name)

        print(" ".join(temp))

        character: int = int(input("character number to be removed\n"))

        if character < self._front:
            self._front -= 1

        self._timeline.pop(character)


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
