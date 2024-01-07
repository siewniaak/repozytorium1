class Student:
    def __init__(self, imie, oceny):
        self.imie = imie
        self.oceny = oceny

    def is_passed(self):
        srednia_ocen = sum(self.oceny) / len(self.oceny)
        return srednia_ocen > 50

student1 = Student("Jan", [60, 70, 80])
student2 = Student("Alicja", [40, 30, 20])

wynik1 = student1.is_passed()
wynik2 = student2.is_passed()

print(f"{student1.imie} zdał/a: {wynik1}")
print(f"{student2.imie} zdał/a: {wynik2}")
