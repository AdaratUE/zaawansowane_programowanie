class Student:
    def __init__(self, name: str, mark: int):
        self.name = name
        self.mark = mark

    def is_passed(self) -> bool:
        if self.mark > 50:
            return True
        else:
            return False


student1 = Student("Adam", 80)
student2 = Student("Jan", 30)

print(student1.is_passed())
print(student2.is_passed())