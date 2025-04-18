def person_info(**kwargs):
    for key in kwargs:
        print(key + ": " + str(kwargs[key]))

person_info(name="Daniil",age=19,country="Kenia")
print()
person_info(name="Alexsosandr",age=18,country="Azerbaijan")