# this is how two or more dictionary can be combined

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

combined_dict = {**dict1, **dict2}
print(f"Combined Dictonary: {combined_dict}")