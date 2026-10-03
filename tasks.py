from crewai import Task
from agents import verification_agent


verification_task = Task(
    description=(
        "Verify the university student with MIS ID: {mis_id}. "
        "Use the Student Record Search tool to search the university "
        "student records. If the MIS ID exists, provide a professional "
        "verification message including the student's name, program, "
        "semester, and status. If the MIS ID does not exist, clearly "
        "state that the student could not be verified and advise the "
        "security officer to contact the university security office."
    ),
    expected_output=(
        "A clear and professional student verification result. "
        "For a valid student, confirm verification and provide the "
        "available student details. For an invalid MIS ID, state that "
        "the student could not be verified."
    ),
    agent=verification_agent
)