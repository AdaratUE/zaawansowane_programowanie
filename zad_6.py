def lists(list1: list, list2: list) -> list:
    list3 = list(dict.fromkeys(list1 + list2))
    for x in range(len(list3)):
        list3[x] = list3[x] ** 3
    return list3


print(lists([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]))
