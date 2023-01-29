import random


def true_shuffle(list_for_shuffle: list) -> list:
    """
    This function carry out shuffle of list elements
    @list_for_shuffle: list

    examples: true_shuffle(['q', 'w', 'e', 'r', 't', 'y'])
             >>> ['w', 't', 'q', 'e', 'y', 'r']
    """
    lenght = len(list_for_shuffle)
    list_of_new_indexes = []
    shuffled_list = []
    while lenght > 0:
        random_num = random.randint(0, len(list_for_shuffle) - 1)
        if random_num not in list_of_new_indexes:
            list_of_new_indexes.append(random_num)
            lenght -= 1
            shuffled_list.append(list_for_shuffle[random_num])
    return shuffled_list
