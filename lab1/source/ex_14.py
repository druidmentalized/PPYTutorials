list_var = [10, "something", 20, "something more"]

# a)
print("All elements except last:", list_var[:-1])

# b)
print("Every second element:", list_var[::2])

# c)
print("Every second element up to the middle:", list_var[:len(list_var) // 2:2])

# d)
x = "something"
print("Is x in the list:", x in list_var)

# e)
print("Tuple vs List: Lists are mutable, Tuples are immutable")

# f)
#   1
list_var.append("new_value")
#   2
list_var.insert(1, "inserted_value")

# g)
list_var.pop()

# h)
list_var.pop(2)

# i)
new_list = ["extra", "values"]
list_var.extend(new_list)
print("Updated list:", list_var)

# j)
print("Count of 'X':", list_var.count("X"))
