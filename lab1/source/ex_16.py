two_dim_list = [
    ["first", "list"],
    ["second", "list"],
    ["third", "list"]
]

print(two_dim_list)
del two_dim_list
try:
    print(two_dim_list)
except:
    print("The list was deleted, it cannot be printed")
