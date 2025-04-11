authenticated = False

def requires_auth(func):
    def wrapper():
        if authenticated:
            func()
        else:
            print("Access denied")
    return wrapper

@requires_auth
def view_profile():
    print("Some profile information to be shown")

view_profile()
print("Changing authentication status...")
authenticated = True
view_profile()