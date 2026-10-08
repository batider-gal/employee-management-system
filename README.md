# Employee Management System (Python OOP)

## Overview

This is a Python-based Employee Management System created to practice Object-Oriented Programming (OOP).

The program allows users to create employees, manage their information, update job levels, assign salaries, and provide bonuses.

This project was originally developed as part of a freeCodeCamp Python OOP exercise and later extended with additional features.

## Features

- **Employee Creation:** Create employees with a name and job level.
- **Salary Management:** Automatically assign salaries based on employee levels.
- **Employee Promotion:** Promote employees to higher job levels.
- **Salary Validation:** Prevent salaries from being set below the minimum for an employee's level.
- **Bonus System:** Give employees salary bonuses.
- **Employee Information:** Display employee names, job levels, and salaries.
- **Employee Counter:** Track the total number of employees created.
- **Error Handling:** Validate inputs and raise appropriate errors.

## Employee Levels and Base Salaries

| Level | Base Salary |
|---|---|
| Trainee | $1,000 |
| Junior | $2,000 |
| Mid-Level | $3,000 |
| Senior | $4,000 |

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Python Standard Library

## OOP Concepts Practiced

- Classes and Objects
- Constructors (`__init__`)
- Encapsulation
- Getters and Setters
- `@property` Decorators
- Instance and Class Attributes
- Magic Methods (`__str__`, `__repr__`)
- Data Validation and Exception Handling

## Example Usage

```python
employee1 = Employee("Charlie Brown", "trainee")

# Display employee information
employee1.display_info()

# Give a bonus
employee1.give_bonus(500)

# Promote employee
employee1.level = "junior"

# Display updated information
employee1.display_info()

# Count employees
print(Employee.employee_count)
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python employee.py
```

## Project Structure

```text
employee-management/
├── employee.py
└── README.md
```

## Learning Outcomes

Through this project, I practiced:

- Creating and managing Python classes and objects.
- Using encapsulation to control access to attributes.
- Implementing getters and setters with properties.
- Validating employee information and salary values.
- Using dictionaries to manage salary structures.
- Extending an existing program with new functionality.

## Future Improvements

- Add a command-line menu for managing multiple employees.
- Allow users to delete employee records.
- Save employee information using JSON or SQLite.
- Add automated unit tests.
- Build a simple graphical or web interface.

## Acknowledgments

The original Employee class was developed through a step-by-step freeCodeCamp Python lesson. Additional features were added with AI assistance to expand the project and practice OOP concepts.
