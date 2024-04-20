from classes import *


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
