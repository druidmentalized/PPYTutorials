import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

text = ("Was justice improve age article between. No projection as up preference reasonably delightful celebrated."
        " Preserved and abilities assurance tolerably breakfast use saw. And painted letters forming far village "
        "elderly compact. Her rest west each spot his and you knew. Estate gay wooded depart six far her. Of we be"
        " have it lose gate bred. Do separate removing or expenses in. Had covered but evident chapter matters anxious.")
print(f"Formatted text: {remove_punctuation(text)}")