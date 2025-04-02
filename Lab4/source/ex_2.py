def sort_by_last_char(strings):
    return sorted(strings, key = lambda string : string[-1])

strings = ["Here", "are", "some", "strings", "that", "we", "are", "working", "with"]
print(f"Before sorting: {strings}")
print(f"After sorting: {sort_by_last_char(strings)}")