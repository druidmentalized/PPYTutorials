import re

def regex_matcher(pattern):
    regex = re.compile(pattern)
    try:
        while True:
            gen_input = yield
            if regex.search(gen_input):
                print(gen_input)
    except GeneratorExit:
        print("Generator exited")

matcher = regex_matcher(r"\berror\b")
next(matcher)

matcher.send("info: everything is fine")
matcher.send("warning: something is weird")
matcher.send("error: something failed")
matcher.send("critical: error occurred again")

matcher.close()