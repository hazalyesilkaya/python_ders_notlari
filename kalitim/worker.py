class Worker:
    day_of = 30

    def __init__(self, name, surname, company, salary, phone):
        self.name = name
        self.surname = surname
        self.company = company
        self.salary = salary
        self.phone = phone
        self.mail = f"{name.lower()}{surname.lower()}@{company.lower()}.com"

    def view_info(self):
        print(f"{self.name} {self.surname} , {self.company}\n{self.phone} , {self.mail}")
        print()


class Programmer(Worker):
    def __init__(self, name, surname, company, salary, phone, branch, langs):
        super().__init__(name, surname, company, salary, phone)
        self.branch = branch
        self.langs = langs

    def get_info(self):
        print(f"{self.name} {self.surname} , {self.company}\n{self.phone} , {self.mail}\n{self.branch}", end=" , ")
        print(f"{self.langs}", end="\n")


class Management(Worker):
    def __init__(self, name, surname, company, salary, phone, team):
        super().__init__(name, surname, company, salary, phone)
        self.team = team

    def view_info(self):
        print(f"{self.name} {self.surname} , {self.company} , {self.phone} , {self.mail} , {self.day_of}", end=" , ")

    def view_team(self):
        for person in self.team:
            print(f"{self.team.index(person)+1} . ", end="")
            person.view_info()

    def add_worker(self, person):
        self.team.append(person)
        print(f"{person.name} isimli çalışan {self.name} isimli yöneticinin çalışma ekibine eklendi.")

    def del_worker(self, person):
        self.team.remove(person)
        print(f"{person.name} isimli çalışan {self.name} isimli yöneticinin çalışma ekibinden çıkarıldı.")

    def create_worker(self, statu="Worker"):
        name = input("Name: ")
        surname = input("Surname: ")
        company = input("Company: ")
        salary = input("Salary: ")
        phone = input("Phone: ")
        if statu == "Programmer":
            person = Worker(name, surname, company, salary, phone)

        else:
            while True:
                statu = input("Statu: ").title()
                if statu == "Programmer":
                    branch = input("Branch: ")
                    langs = ["Phyton", "Java", "PHP", "C#"]
                    person = Programmer(name, surname, company, salary, phone, branch, langs)
                    break
                else:
                    print("Geçersiz statu")

        self.add_worker(person)


yunus = Worker("Yunus", "Alparslan", "Ecodation", 111111, 5559996633)
yakup = Worker("Yasin", "Kara", "Turkcell", 222222, 5557774411)

yunus.view_info()
yakup.view_info()

hazal = Programmer("Yunus", "Alparslan", "Ecodation", 111111, 5559996633, "Programmer", "PHP")
oguz = Programmer("Yasin", "Kara", "Turkcell", 222222, 5557774411, "Programmer", "C#")

hazal.get_info()
oguz.get_info()

management1 = Management("management1", "Alparslan", "Ecodation", 111111, 5559996633, [yunus, yakup])
management2 = Management("management1", "Alparslan", "Ecodation", 111111, 5559996633, [yunus, yakup])
management2.create_worker()
management1.view_info()
print("\n---------------")
management1.view_team()