def even_filter(input_list):
    return [num for num in input_list if num % 2 == 0]
def odd_filter(input_list):
    return [num for num in input_list if num % 2 != 0]
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dictionary_of_numbers = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

even_numbers = even_filter(list_of_numbers)
print("Even numbers from list:", even_numbers)

odd_numbers_dict = odd_filter(list(dictionary_of_numbers.values()))
print("Odd numbers from the dictionary:", odd_numbers_dict)
