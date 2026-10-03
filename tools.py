
import json
from pathlib import Path
from crewai.tools import BaseTool


class StudentVerificationTool(BaseTool):
    name: str = "Student Record Search"
    description: str = (
        "Searches university student records using a numeric MIS ID "
        "and returns the student's complete verification information."
    )

    def _run(self, mis_id: str) -> str:
        file_path = Path(__file__).parent / "data" / "students.json"

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                students = json.load(file)

            mis_id = str(mis_id).strip()

            for student in students:
                if student["mis_id"] == mis_id:
                    return (
                        f"VERIFIED: "
                        f"MIS ID: {student['mis_id']}, "
                        f"Name: {student['name']}, "
                        f"Program: {student['program']}, "
                        f"Semester: {student['semester']}, "
                        f"Status: {student['status']}."
                    )

            return f"NOT VERIFIED: No student record found for MIS ID {mis_id}."

        except FileNotFoundError:
            return "ERROR: Student records file was not found."

        except Exception as e:
            return f"ERROR: Unable to search student records. {str(e)}"
