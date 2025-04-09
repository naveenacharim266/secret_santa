import random
from typing import List, Dict
from models import Employee
import pandas as pd

class SecretSanta:
    def __init__(self, employees: List[Employee], previous_assignments: Dict[str, str]):
        self.employees = employees
        self.previous_assignments = previous_assignments

    def assign_secret_santa(self):
        available_children = [e for e in self.employees]
        random.shuffle(available_children)

        for giver in self.employees:
            potential_children = [c for c in available_children if c.name != giver.name and c.name != self.previous_assignments.get(giver.name)]

            if not potential_children:
                raise ValueError("No valid Secret Santa assignments possible. Try again!")

            secret_child = random.choice(potential_children)
            giver.secret_child = secret_child
            available_children.remove(secret_child)

    def export_assignments(self, output_file: str):
        data = [
            {
                "Employee_Name": giver.name,
                "Employee_EmailID": giver.email,
                "Secret_Child_Name": giver.secret_child.name,
                "Secret_Child_EmailID": giver.secret_child.email,
            }
            for giver in self.employees
        ]
        df = pd.DataFrame(data)
        df.to_excel(output_file, index=False)