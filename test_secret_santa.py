import unittest
from models import Employee
from logic import SecretSanta

class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        self.employees = [
            Employee("Alice", "alice@example.com"),
            Employee("Bob", "bob@example.com"),
            Employee("Charlie", "charlie@example.com")
        ]
        self.previous_assignments = {
            "Alice": "Bob",
            "Bob": "Charlie",
            "Charlie": "Alice"
        }

    def test_valid_assignments(self):
        ss = SecretSanta(self.employees, self.previous_assignments)
        ss.assign_secret_santa()
        assignments = {e.name: e.secret_child.name for e in self.employees}

        for giver in self.employees:
            child = giver.secret_child
            self.assertIsNotNone(child)
            self.assertNotEqual(giver.name, child.name, "Assigned self")
            self.assertNotEqual(child.name, self.previous_assignments.get(giver.name), "Repeat from last year")

    def test_insufficient_employees(self):
        small_list = [Employee("OnlyOne", "one@example.com")]
        with self.assertRaises(ValueError):
            ss = SecretSanta(small_list, {})
            ss.assign_secret_santa()

    def test_export_assignments(self):
        ss = SecretSanta(self.employees, {})
        ss.assign_secret_santa()
        output_path = "test_assignments.xlsx"
        ss.export_assignments(output_path)

        # Check that the file is written (not reading content here for simplicity)
        import os
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)  # Clean up

if __name__ == '__main__':
    unittest.main()
