def merge_lists(keys, values):
    if len(keys) != len(values):
        return None
    merged_dict = {}
    for i in range(len(keys)):
        merged_dict[keys[i]] = values[i]
    return merged_dict
key_list = input("Enter the unique key list(separated by spaces): ").split()
value_list = input("Enter a list of values (separated by spaces): ").split()
if len(key_list) != len(value_list):
    print("Both lists should be of the same size.")
merged_dict = merge_lists(key_list, value_list)
if merged_dict:
    print("dictionary:", merged_dict)
else:
    print("Lists should contain unique elements \n be of the same size.")

