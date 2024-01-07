class library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"library: {self.city},{self.street}," \
               f"{self.zip_code}\nOpen hours: " \
               f"{self.open_hours}\nTelephone: {self.phone}"


class employee:
    def __init__(self, first_name, last_name,
                 hire_date, birth_date, city,
                 street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} " \
               f"{self.last_name}\nHire date: " \
               f"{self.hire_date}\nBirth date: " \
               f"{self.birth_date}\nLocation: " \
               f"{self.city}, {self.street}, " \
               f"{self.zip_code}\nPhone: {self.phone}"


class book:
    def __init__(self, library, publication_date,
                 author_name, author_surname,
                 number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublished: " \
               f"{self.publication_date}\nPages: " \
               f"{self.number_of_pages}\n{self.library}"


class order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"  - {book}"
                               for book in self.books])
        return f"Order:\n{self.employee}\nStudent: " \
               f"{self.student}\nOrder date: " \
               f"{self.order_date}\nBooks:{book_list}"


library1 = library("Katowice", "Katowicka 1", "30-334",
                   "8:00 - 20:00", "+123456789")
library2 = library("Jaworzno", "Jaworznicka 2", "20-323",
                   "10:00 - 22:00", "+987654321")

employee1 = employee("Patryk", "Patrykowski", "2020-01-01",
                     "2004-01-02", "Jaworzno", "3 Maja",
                     "20-233", "+111222333")
employee2 = employee("Wiktor", "Swoboda", "2021-01-01", "2000-01-01",
                     "Chorzów", "Senna", "30-00", "+444555666")
employee3 = employee("Eustachy", "Sedorf", "2020-02-01", "2001-01-01",
                     "Chrzanów", "Leśna", "12-345", "+777888999")

book1 = book(library1, "2021-01-01",
             "Daniel", "Kowalski", 299)
book2 = book(library1, "2022-02-02",
             "Euzebio", "Gollero", 232)
book3 = book(library2, "2020-03-03",
             "Julhian", "Alvarez", 320)
book4 = book(library2, "2021-04-04",
             "Depay", "Memphis", 160)
book5 = book(library2, "2022-05-05",
             "Olbrzym", "Cieniutki", 170)

order1 = order(employee1, "Student1",
               [book1, book3, book5], "2023-01-15")
order2 = order(employee2, "Student2",
               [book2, book4], "2023-02-20")

print(order1)
print("\n---------------------------\n")
print(order2)
