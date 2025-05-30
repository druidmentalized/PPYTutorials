class UserInputValidator:
    @staticmethod
    def get_age() -> int:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Invalid input.")
            return -1

print(f"Age of integer is: {"Fine" if UserInputValidator.get_age() >= 0 else "Not fine"}")
print(f"Age of string is: {"Fine" if UserInputValidator.get_age() >= 0 else "Not fine"}")