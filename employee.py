
class Employee:
    employee_count = 0  # NEW FEATURE 3: Employee counter

    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.salary = Employee._base_salaries[level]
        Employee.employee_count += 1

    def __str__(self):
        return f'{self.name}: {self.level}'

    def __repr__(self):
        return f"Employee({self.name!r}, {self.level!r})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")

        if new_level not in Employee._base_salaries:
            raise ValueError(
                f"Invalid value '{new_level}' for 'level' attribute."
            )

        if hasattr(self, '_level'):
            if new_level == self.level:
                raise ValueError(
                    f"'{self.level}' is already the selected level."
                )

            if Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
                raise ValueError("Cannot change to lower level.")

            print(f"'{self.name}' promoted to '{new_level}'.")
            self._level = new_level
            self.salary = Employee._base_salaries[new_level]

        else:
            self._level = new_level

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")

        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(
                f"Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}."
            )

        self._salary = new_salary
        print(f"Salary updated to ${self.salary}.")

    def give_bonus(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Bonus must be a positive number.")

        self.salary += amount
        print(f"{self.name} received a ${amount} bonus.")

    def display_info(self):
        print("----- Employee Information -----")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Salary: ${self.salary}")
        print("--------------------------------")


employee1 = Employee("Charlie Brown", "trainee")
employee2 = Employee("Jack Smith", "junior")

employee1.display_info()

employee1.give_bonus(500)

employee1.level = "junior"

employee1.display_info()

print(f"Total employees: {Employee.employee_count}")
