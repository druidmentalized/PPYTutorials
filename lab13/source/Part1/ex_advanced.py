class Dog:
    dog_count = 0
    names_list: list[str] = []

    def __init__(self, name: str) -> None:
        self.name = name
        Dog.dog_count += 1
        Dog.names_list.append(name)

    @staticmethod
    def show_created_count():
        print(f"{Dog.dog_count} were created so far.")

    @staticmethod
    def print_all_names():
        for name in Dog.names_list:
            print(name)


# a)
dog1 = Dog("Dog1")
dog2 = Dog("Dog2")
dog3 = Dog("Dog3")
Dog.print_all_names()
