class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


worker1 = Position("Ivan", "Ivanov", "Manager", 1000, 500)
print(worker1.name)
print(worker1.surname)
print(worker1.position)
print(worker1._income.get("wage"))
print(worker1._income.get("bonus"))
print(worker1.get_full_name())
print(worker1.get_total_income())