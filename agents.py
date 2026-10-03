import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import StudentVerificationTool

load_dotenv()


groq_llm = LLM(
    model="groq/openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)


verification_agent = Agent(
    role="University Student Verification Officer",

    goal=(
        "Verify university students accurately using their numeric MIS ID "
        "and the university student records."
    ),

    backstory=(
        "You are a professional AI-powered university gate verification "
        "officer. Your responsibility is to search student records using "
        "the provided MIS ID and clearly determine whether the student "
        "can be verified."
    ),

    tools=[StudentVerificationTool()],

    llm=groq_llm,

    verbose=True
)