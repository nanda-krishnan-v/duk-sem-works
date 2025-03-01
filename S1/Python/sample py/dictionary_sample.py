def dicti(dictionary):
    print("Original Dictionary:")
    print(dictionary)

    value_sum = sum(dictionary.values())
    print("Sum of values:", value_sum)

    max_key = max(dictionary, key=dictionary.get)
    print("Key with maximum value:", max_key)

    squared_dict = {key: value**2 for key, value in dictionary.items()}
    print("Dictionary with squared values:")
    print(squared_dict)

my_dict = {"a": 5, "b": 10, "c": 15}
dicti(my_dict)

