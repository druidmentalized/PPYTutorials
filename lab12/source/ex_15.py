class GradeTooLowError(Exception):
    pass

class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade

    def check_grade(self) -> None:
        if self.grade < 40:
            raise GradeTooLowError("Grade of checked student is too low.")
        else:
            print(f"Grade of {self.name} is fine.")


good_student = Student("Good", 100)
bad_student = Student("Bad", 39)

good_student.check_grade()
bad_student.check_grade()