from backend.job_search import search_jobs


jobs = search_jobs(
    query="Python Developer",
    location="Bangalore"
)

print(f"\nFound {len(jobs)} jobs\n")

for job in jobs:
    print("=" * 60)
    print("TITLE:", job["title"])
    print("COMPANY:", job["company"])
    print("LOCATION:", job["location"])
    print("SALARY:", job["salary_min"], "-", job["salary_max"])
    print("APPLY:", job["url"])
