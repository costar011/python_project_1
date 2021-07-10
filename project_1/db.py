# SingleTone
# 내부에서는 제어 가능 하지만 외부에서는 제어 못함

# Object 객체
class Person:
    name = ""
    age = 0
    gender = ""

    # 데이터를 넣는 기능
    def data_setter(self, p1, p2, p3):
        self.name = p1
        self.age = p2
        self.gender = p3

    # __str__ 은
    def __str__(self):
        return f"{self.name} | {self.age} | {self.gender}"

    def add_age(self):
        self.age = self.age + 1
