import os

from crewai import Agent, Crew, Task, LLM
from crewai.tools import tool

from backend.job_search import search_jobs
from backend.resume_analyzer import create_resume_task


def create_llm():

    return LLM(
        model="gemini/gemini-3.5-flash-lite",
        api_key=os.getenv("GEMINI_API_KEY")
    )


@tool("Job Search")
def job_search(query: str, location: str = "India") -> str:
    """
    Search real job listings using Adzuna.

    The query can be ANY type of job title or keyword.
    """

    try:

        jobs = search_jobs(
            query=query,
            location=location,
            results_per_page=10
        )

        if not jobs:
            return (
                f"No jobs found for '{query}' "
                f"in '{location}'."
            )

        results = []

        for job in jobs:

            results.append(
                f"""
TITLE: {job.get('title', 'Unknown')}

COMPANY: {job.get('company', 'Unknown')}

LOCATION: {job.get('location', 'Unknown')}

SALARY: {job.get('salary_min', 'N/A')} - {job.get('salary_max', 'N/A')}

DESCRIPTION: {job.get('description', '')}

URL: {job.get('url', '')}
"""
            )

        return "\n-----------------------------\n".join(results)

    except Exception as e:

        return f"Job search failed: {str(e)}"


def analyze_resume(resume_text):

    llm = create_llm()

    # -------------------------
    # Resume Analyzer
    # -------------------------

    analyzer = Agent(
        role="Resume Analyzer",

        goal="""
        Carefully analyze the candidate's resume and identify
        their skills, experience, previous roles, projects,
        suitable job titles, and location.
        """,

        backstory="""
        You are an expert resume analyst.

        You only use information supported by the resume.

        You can identify suitable jobs from ANY profession.
        Do not restrict the candidate to technology jobs.
        Do not use a predefined list of job titles.
        """,

        llm=llm,

        verbose=True
    )

    # -------------------------
    # Job Hunter
    # -------------------------

    hunter = Agent(
        role="Job Hunter",

        goal="""
        Find real job openings that match the candidate's
        resume and suitable job titles.
        """,

        backstory="""
        You are an experienced job search specialist.

        You use the Job Search tool to find real current
        job listings.

        You can search for jobs from ANY profession.

        Only report jobs that are returned by the Job Search tool.
        """,

        tools=[job_search],

        llm=llm,

        verbose=True
    )

    # -------------------------
    # Resume analysis task
    # -------------------------

    resume_task = create_resume_task(
        agent=analyzer
    )

    # -------------------------
    # Job hunting task
    # -------------------------

    hunt_task = Task(

        description="""
        Use the candidate resume and the resume analysis
        to find suitable real job openings.

        First identify the suitable job titles from the
        resume analysis.

        Then use the Job Search tool to search for each
        suitable job title.

        Use the candidate's location if it is explicitly
        available in the resume.

        If no location is available, search in India.

        Search multiple suitable job titles rather than
        searching only one title.

        Do not restrict searches to any predefined profession.

        Only report jobs that were actually returned by
        the Job Search tool.

        Return the job title, company, location, salary
        when available, description, and application URL.
        """,

        expected_output="""
        A list of real job openings found using the
        Job Search tool.

        For every job include:

        - Job title
        - Company
        - Location
        - Salary if available
        - Description
        - Application URL
        """,

        agent=hunter
    )

    # -------------------------
    # Create Crew
    # -------------------------

    crew = Crew(
        agents=[
            analyzer,
            hunter
        ],

        tasks=[
            resume_task,
            hunt_task
        ],

        verbose=True
    )

    # -------------------------
    # Run Crew
    # -------------------------

    result = crew.kickoff(
        inputs={
            "resume": resume_text
        }
    )

    print("\n========== FINAL CREW RESULT ==========\n")
    print(result)
    print("\n=======================================\n")

    return str(result)