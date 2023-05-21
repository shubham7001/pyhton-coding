#Write a Python script to merge two Python dictionaries.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merging dictionaries using the update() method
merged_dict = dict1.copy()
merged_dict.update(dict2)

# Printing the merged dictionary
print("Merged dictionary:", merged_dict)
