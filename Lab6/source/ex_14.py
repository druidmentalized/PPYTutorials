import string

def convert_dates(text):
    words = text.split()
    for i, word in enumerate(words):
        clean = word.strip(string.punctuation)
        if len(clean) == 10 and clean[2] == '/' and clean[5] == '/':
            month, day, year = clean[:2], clean[3:5], clean[6:]
            if month.isdigit() and day.isdigit() and year.isdigit():
                words[i] = word.replace(clean, f"{year}-{month}-{day}")
    return ' '.join(words)

test_string = ("Some of the dates, which are going to be formatted by the"
               " function above: 28/09/1944, 13/11/1997, 15/04/1916, 21/06/1989, 10/08/1984")
print(f"Working with: {test_string}")
print(f"Result: {convert_dates(test_string)}")