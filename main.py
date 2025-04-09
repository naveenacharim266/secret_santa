from utils import read_employees, read_previous_assignments
from logic import SecretSanta


def main():
    employee_file = './Employee-List.xlsx'
    prev_assignments_file = './Secret-Santa-Game-Result-2023.xlsx'
    output_file = './secret_santa_assignments.xlsx'

    employees = read_employees(employee_file)
    previous_assignments = read_previous_assignments(prev_assignments_file)

    secret_santa = SecretSanta(employees, previous_assignments)
    secret_santa.assign_secret_santa()
    secret_santa.export_assignments(output_file)

    print("Secret Santa assignments generated successfully!")


if __name__ == "__main__":
    main()