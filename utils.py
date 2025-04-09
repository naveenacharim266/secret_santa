import pandas as pd
from typing import List, Dict
from models import Employee

def read_employees(input_file: str) -> List[Employee]:
    df = pd.read_excel(input_file)
    return [Employee(row['Employee_Name'], row['Employee_EmailID']) for _, row in df.iterrows()]

def read_previous_assignments(prev_file: str) -> Dict[str, str]:
    try:
        df = pd.read_excel(prev_file)
        return {row['Employee_Name']: row['Secret_Child_Name'] for _, row in df.iterrows()}
    except FileNotFoundError:
        print("Previous assignments file not found. Proceeding without constraints.")
        return {}
