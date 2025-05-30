class Person:
    def __init__(self, name: str, surname: str, birth_year: int):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def describe(self):
        print(f"Description:\n\tName={self.name},\n\tSurname={self.surname},\n\tBirthYear={self.birth_year}")

class Student(Person):
    student_id: int

    def __init__(self, name: str, surname: str, birth_year: int, student_id: int):
        super().__init__(name, surname, birth_year)
        self.student_id = student_id

    def describe(self):
        super().describe()
        print(f"\tStudent_id={self.student_id}")

person = Person("Dmitriy", "Barmuta", 2006)
person.describe()
student = Student("Dmitriy", "Barmuta", 2006, 29871)
student.describe()