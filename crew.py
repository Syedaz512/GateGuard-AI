import crewai.llms.cache as _crewai_cache

# Fix for CrewAI + Groq cache_breakpoint compatibility
_crewai_cache.mark_cache_breakpoint = lambda msg: msg

from crewai import Crew, Process
from agents import verification_agent
from tasks import verification_task


def verify_student(mis_id):
    crew = Crew(
        agents=[verification_agent],
        tasks=[verification_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(
        inputs={"mis_id": str(mis_id)}
    )

    return result