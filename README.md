# Secret Santa Assignment - DigitalXC Challenge

This project implements a modular, extensible, and testable solution for the Secret Santa pairing challenge using Python.

---

##  Project Structure

```
secret_santa/
├── main.py                             # Entry point of the program
├── models.py                           # Employee model class
├── logic.py                            # SecretSanta logic class
├── utils.py                            # Functions for reading Excel files
├── test_secret_santa.py                # Unit tests for logic and utils
├── Employee-List.xlsx                  # Input file with employee name and email
├── Secret-Santa-Game-Result-2023.xlsx  # Optional: Last year's assignments
└── secret_santa_assignments.xlsx       # Output file generated
```

---

##  Requirements

- Python 3.7+
- `pandas`
- `openpyxl` (Excel reader for pandas)

Install dependencies:
```bash
pip install pandas openpyxl
```

---

##  Cloning the Repository

To pull and run this project on a new system:

```bash
git clone https://github.com/naveenacharim266/secret_santa.git
cd secret_santa
pip install pandas openpyxl
python main.py
```

---

##  Running the Program

Place your Excel files (`Employee-List.xlsx`, `Secret-Santa-Game-Result-2023.xlsx`) in the same directory.
Run the following command:

```bash
python main.py
```

The program will:
- Read employee list
- Check past assignments to avoid repeats
- Generate valid Secret Santa pairs
- Export the results to `secret_santa_assignments.xlsx`

---

##  Features

- OOP-based structure with extensibility for future enhancements
- Clean separation of concerns (models, logic, I/O)
- Reads and writes `.xlsx` files
- Error handling for file errors and invalid assignment states
- Ready-to-run with test data

---

##  Tests
Run unit tests with:
```bash
python -m unittest test_secret_santa.py
```

Test coverage includes:
- Employee creation
- Logic for assigning unique secret child
- Handling edge cases (e.g. not enough employees)

---

##  Extending This Project

You can easily add:
- Web interface (Flask/Django)
- Email notification system
- Admin dashboard for assignment visualization
- CLI support for file paths and year input

---

##  Notes
- Ensure employee names are unique across years.
- Assignment logic avoids assigning the same child from previous year and self.
- Raise issues if any assignment isn't possible.

---

