class Employee:
    def __init__(self, name, salary, supervisor=None):
        self.name = name
        self.salary = salary
        self.supervisor = supervisor

        if self.supervisor is not None:
            self.supervisor.add_employee(self)

    def __str__(self):
        info = self.__class__.__name__
        info += f": {self.name}, {self.salary}"
        return info

    def print_supervisor(self):
        if self.supervisor is None:
            print(f"{self.name} has no supervisor")
        else:
            print(self.supervisor)

    def set_supervisor(self, emp):
        if not isinstance(emp, Manager):
            print(f"{emp} is not a manager")
            return
        emp.add_employee(self)
        self.supervisor = emp


class Manager(Employee):
    def __init__(self, name, salary, supervisor=None):
        super().__init__(name, salary, supervisor)
        self.employee_list = []
        self.supervisor = None

    def print_employees(self):
        print(f"Employees supervised by {self.name}")
        for emp in self.employee_list:
            print(emp)

    def add_employee(self, emp):
        self.employee_list.append(emp)


class Engineer(Employee):
    def __init__(self, name, salary, supervisor=None):
        super().__init__(name, salary, supervisor)
        self.project_names = []

    def print_working_projects(self):
        print(f"Projects that {self.name} works on:")
        print(self.project_names)

    def add_project(self, name):
        self.project_names.append(name)


class SalesPerson(Employee):
    def __init__(self, name, salary, supervisor=None):
        super().__init__(name, salary, supervisor)
        self.profit = 0

    def make_sale(self, amount):
        self.profit += amount

    def print_profit_made(self):
        print(f"Profit made by {self.name}:")
        print(self.profit)


if __name__ == "__main__":
    manager = Manager("1", 100)
    engineer = Engineer("2", 90, manager)
    salesperson = SalesPerson("3", 80, manager)

    manager.print_employees()
    manager.print_supervisor()
    print()

    engineer.add_project("Ex4")
    engineer.print_working_projects()
    engineer.print_supervisor()
    print()

    salesperson.make_sale(100)
    salesperson.print_profit_made()