def inverse_case(string):
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)

test_string = "Some test STRING tO TeSt working AbIlItY oF tHe ProGRam"
print(f"Working with: {test_string}")
print(f"Result: {inverse_case(test_string)}")
