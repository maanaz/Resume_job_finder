from crewai import Task


def create_resume_task(agent):

    return Task(
        description="""
        Analyze the following resume.

        Resume:

        {resume}

        Extract only information that is explicitly supported
        by the resume.

        Return:

        1. Technical skills

        2. Experience level

        3. Technologies

        4. Areas of strongest experience

        5. Previous job roles

        6. Projects and relevant experience

        7. Suitable job titles

        8. Candidate location

        For "Suitable job titles":

        - Suggest 3 to 5 job titles that reasonably match the
          candidate's actual skills, experience, education and
          projects.
        - Job titles can belong to ANY profession.
        - Do not restrict the suggestions to technology jobs.
        - Do not use a predefined list of job titles.
        - Do not invent skills or experience.

        For "Candidate location":

        - Extract the location only if it is explicitly present
          in the resume.
        - If no location is present, return "India".

        Do not invent information.
        """,

        expected_output="""
        A candidate profile containing:

        - technical skills
        - experience level
        - technologies
        - strongest areas
        - previous roles
        - relevant projects and experience
        - 3 to 5 suitable job titles
        - candidate location
        """,

        agent=agent
    )