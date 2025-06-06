class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name # Public
        self._age = age # Protected
        self.__ssn = "123-45-6789" # Private
        
# a)
person = Person("Dmitriy", 30)

# b)
print(f"Name: {person.name}")       
print(f"Age: {person._age}")

# c)
try:
    print(person.__ssn)
except AttributeError as e:
    print("Error accessing __ssn directly:", e)

# d)
print(f"SSN (via name mangling): {person._Person__ssn}")