class Character:
    def __init__(self, name, speed):
        self.name: str = name
        self.speed: float | int = speed

    def __lt__(self, other):
        return self.speed < other.speed


class Timeline:
    def __init__(self, lst: list[Character]):
        self._timeline = []
        self._front = 0
        for character in lst:
            self._timeline.append(character.name)

    def print(self):
        if self._front == 0:
            print("--".join(self._timeline))
        else:
            print("--".join(self._timeline[self._front:]) + "--" + "--".join(self._timeline[:self._front]))

    def next_round(self):
        self._front += 1

        if self._front >= len(self._timeline):
            self._front -= len(self._timeline)

    def remove(self):
        print(self._timeline)

        character = input("character to be removed\n")

        if self._timeline.index(character) < self._front:
            self._front -= 1

        self._timeline.remove(character)



def main():
    return


if __name__ == "__main__":
    main()
