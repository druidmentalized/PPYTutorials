import re

def extract_emails(text):
    return re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

test_text = "Contact me at jane.doe@example.com, dmitriy.barmuta@gmail.com or s29871@pjwstk.edu.pl"
print(f"Working with: {test_text}")
print(f"Result: {extract_emails(test_text)}")