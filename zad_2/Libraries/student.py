class Student:
    def __init__(self, student_name: str, student_surname: str, student_id: int) -> object:
        self.student_name = student_name
        self.student_surname = student_surname
        self.student_id = student_id

    def __str__(self):
        return f'{self.student_surname} {self.student_name} o numerze {self.student_id}'
