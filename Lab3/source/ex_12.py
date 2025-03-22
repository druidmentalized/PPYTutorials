def greet(*args, **kwargs):
    greeting = kwargs.get("greeting", "Wassup")
    punctuation = kwargs.get("punctuation", ".")

    for name in args:
        print(f"{greeting}, {name}{punctuation}")

greet("Aleksandr Biktimirov", greeting="Hi", punctuation="!")
greet("Danyil Danillian", greeting="How are you doing", punctuation="?")