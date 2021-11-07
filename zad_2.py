#w forze
def names_for_function(list_of_numbers: list):
    for x in range(len(list_of_numbers)):
        list_of_numbers[x] = list_of_numbers[x] * 2
    return list_of_numbers

#w liście składanej
def names_list_function(list_of_numbers: list):
    return [num * 2 for num in list_of_numbers]


numbers = [1, 2, 3, 4, 5]

numbers = names_list_function(numbers)

print(numbers)