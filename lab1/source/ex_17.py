dictionary_var = {
    "test1": 1,
    "test2": 3.14,
    "test3": "value",
    "test4": True,
    "test5": ["yes", "this", "is", "list", "inside", "dictionary"]
}

# a)
print(f"All keys of the created dictionary: {dictionary_var.keys()}")

# b)
del dictionary_var["test1"]
print(f"Dictionary with deleted value: {dictionary_var}")

# c)
dictionary_var["test6"] = "new value"
print(f"Dictionary with updated value: {dictionary_var}")
