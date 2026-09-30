import os
import requests
from dotenv import load_dotenv

load_dotenv()


def search_jobs(query, location, results_per_page=20):
    """
    Search for jobs using Adzuna.

    Parameters:
        query: Job title or keyword
        location: City or location
        results_per_page: Number of jobs to return

    Returns:
        List of job dictionaries
    """

    adzuna_id = os.getenv("ADZUNA_ID")
    adzuna_key = os.getenv("ADZUNA_KEY")

    if not adzuna_id or not adzuna_key:
        raise ValueError(
            "ADZUNA_ID and ADZUNA_KEY are missing from .env"
        )

    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"


    params = {
        "app_id": adzuna_id,
        "app_key": adzuna_key,
        "what": query,
        "where": location,
        "results_per_page": results_per_page,
        "content-type": "application/json"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(
            f"Adzuna API error: {response.status_code}\n"
            f"{response.text}"
        )

    data = response.json()

    jobs = []

    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "url": job.get("redirect_url")
        })

    return jobs