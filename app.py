import streamlit as st
from dotenv import load_dotenv

from backend.job_search import search_jobs
from backend.crew import analyze_resume
from utils.pdf_reader import extract_text_from_pdf

load_dotenv()
 
 
st.set_page_config( 
    page_title="Job Finder", 
    page_icon="💼", 
    layout="wide" 
) 
 
st.title("💼 Job Finder") 
st.write("Search for real job listings using Adzuna.") 
 
 
# ------------------------- 
# Search section 
# ------------------------- 
 
st.header("Search Jobs") 
 
query = st.text_input( 
    "Job title or keyword", 
    placeholder="Example: Python Developer" 
) 
 
location = st.text_input( 
    "Location", 
    placeholder="Example: Bangalore" 
) 
 
search_button = st.button( 
    "🔎 Search Jobs", 
    type="primary" 
) 
 
 
# ------------------------- 
# Search results 
# ------------------------- 
 
if search_button: 
 
    if not query: 
        st.warning("Please enter a job title or keyword.") 
 
    elif not location: 
        st.warning("Please enter a location.") 
 
    else: 
 
        with st.spinner("Searching for jobs..."): 
 
            try: 
                jobs = search_jobs( 
                    query=query, 
                    location=location, 
                    results_per_page=20 
                ) 
 
                st.session_state["jobs"] = jobs 
 
            except Exception as e: 
                st.error(f"Something went wrong: {e}") 
 
 
# ------------------------- 
# Display jobs 
# ------------------------- 
 
if "jobs" in st.session_state: 
 
    jobs = st.session_state["jobs"] 
 
    st.subheader(f"Found {len(jobs)} jobs") 
 
    if not jobs: 
 
        st.info("No jobs found. Try a different search.") 
 
    else: 
 
        for job in jobs: 
 
            st.markdown("---") 
 
            st.subheader(job["title"]) 
 
            st.write( 
                f"🏢 **Company:** {job['company'] or 'Not specified'}" 
            ) 
 
            st.write( 
                f"📍 **Location:** {job['location'] or 'Not specified'}" 
            ) 
 
            if job["salary_min"] or job["salary_max"]: 
 
                st.write( 
                    f"💰 **Salary:** " 
                    f"{job['salary_min'] or 'N/A'} - " 
                    f"{job['salary_max'] or 'N/A'}" 
                ) 
 
            description = job["description"] or "" 
 
            st.write(description) 
 
            if job["url"]: 
 
                st.link_button( 
                    "Apply / View Job", 
                    job["url"] 
                ) 

# -------------------------
# Resume-based job search
# -------------------------

st.markdown("---")

st.header("📄 Find Jobs Using Your Resume")

uploaded_resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

if uploaded_resume:

    if st.button(
        "🔍 Find Jobs From Resume",
        type="primary"
    ):

        with st.spinner(
            "Analyzing your resume and finding suitable jobs..."
        ):

            try:

                # -------------------------
                # Save uploaded PDF
                # -------------------------

                with open("uploaded_resume.pdf", "wb") as f:
                    f.write(
                        uploaded_resume.getbuffer()
                    )

                # -------------------------
                # Extract resume text
                # -------------------------

                resume_text = extract_text_from_pdf(
                    "uploaded_resume.pdf"
                )

                if not resume_text.strip():

                    st.error(
                        "Could not read the uploaded resume."
                    )

                else:

                    # -------------------------
                    # Analyze resume + find jobs
                    # -------------------------

                    result = analyze_resume(
                        resume_text
                    )

                    # Store CrewAI result
                    st.session_state[
                        "resume_jobs"
                    ] = str(result)

                    st.success(
                        "Jobs found successfully!"
                    )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# -------------------------
# Display resume-based jobs
# -------------------------

if "resume_jobs" in st.session_state:

    st.markdown("---")

    st.subheader(
        "🎯 Jobs Found From Your Resume"
    )

    result = st.session_state[
        "resume_jobs"
    ]

    if not result:

        st.info(
            "No matching jobs were found."
        )

    else:

        st.markdown(result)