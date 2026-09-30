# 💼 Job Finder

An AI-powered job search application that allows users to search for real job openings manually or find suitable jobs based on their resume.

The application combines **Streamlit**, **CrewAI**, **Google Gemini**, and the **Adzuna Jobs API** to search and present real job listings.

---

## 🚀 Features

### 🔎 Manual Job Search

Search for jobs using:

* Job title or keyword
* Location

Example:

```text
Job: Python Developer
Location: Bangalore
```

The application retrieves real job listings from Adzuna.

### 📄 Resume-Based Job Search

Users can upload their resume as a PDF.

The application then:

```text
Resume PDF
    ↓
PDF text extraction
    ↓
CrewAI Resume Analyzer
    ↓
Skills / experience / suitable job titles / location
    ↓
CrewAI Job Hunter
    ↓
Adzuna Job Search Tool
    ↓
Real job listings
```

The resume is analyzed internally and is used to identify suitable job searches.

### 🌐 Real Job Listings

Job results include information such as:

* Job title
* Company
* Location
* Salary when available
* Job description
* Application URL

Users can directly open the original job listing.

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI / LLM

* CrewAI
* Google Gemini

### Job Search

* Adzuna Jobs API

### Backend

* Python
* Requests

### Resume Processing

* PyPDF

---

## 📁 Project Structure

```text
Resume_job_finder/
│
├── .env
├── .gitignore
├── app.py
├── test_adzuna.py
├── test_job_search.py
│
├── backend/
│   ├── __init__.py
│   ├── job_search.py
│   ├── resume_analyzer.py
│   └── crew.py
│
└── utils/
    ├── __init__.py
    └── pdf_reader.py
```

### Important files

**`app.py`**

Main Streamlit application.

**`backend/job_search.py`**

Connects to the Adzuna API and retrieves job listings.

**`backend/resume_analyzer.py`**

Defines the CrewAI task used to analyze uploaded resumes.

**`backend/crew.py`**

Contains the CrewAI agents, tasks, and Adzuna job-search tool.

**`utils/pdf_reader.py`**

Extracts text from uploaded PDF resumes.

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd Resume_job_finder
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
ADZUNA_ID=your_adzuna_app_id
ADZUNA_KEY=your_adzuna_app_key
```

### Important

Never commit `.env` to GitHub.

Make sure `.gitignore` contains:

```text
.env
.venv/
__pycache__/
```

---

## ▶️ Run the Application

Start Streamlit with:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 🧠 How the AI Workflow Works

For resume-based searches, the application uses two CrewAI agents.

### 1. Resume Analyzer

The Resume Analyzer examines the uploaded resume and identifies information such as:

* Skills
* Technologies
* Experience
* Previous roles
* Projects
* Suitable job titles
* Candidate location

It only uses information supported by the uploaded resume.

### 2. Job Hunter

The Job Hunter receives the resume analysis and searches for suitable real job openings.

It uses the custom **Job Search** tool, which connects to the Adzuna API.

```text
Resume Analyzer
       ↓
Resume analysis
       ↓
Job Hunter
       ↓
Job Search Tool
       ↓
Adzuna API
       ↓
Real job listings
```

---

## 🔎 Manual Search vs Resume Search

The application supports two different workflows.

### Manual Search

```text
User
 ↓
Job title + location
 ↓
Adzuna
 ↓
Job listings
```

No resume is required.

### Resume Search

```text
User
 ↓
Upload resume
 ↓
Resume Analyzer
 ↓
Job Hunter
 ↓
Adzuna
 ↓
Job listings
```

This allows the application to work as a general-purpose job finder while also providing personalized resume-based searching.

---

## 🧪 Testing

The project includes scripts for testing the job-search functionality.

Run:

```bash
python test_job_search.py
```

This tests the Adzuna job search integration.

---

## 🔐 Security

API credentials are stored in environment variables rather than directly in the source code.

Do not commit:

```text
.env
```

to the repository.

If an API key is accidentally exposed, revoke it and generate a new one.

---

## 📌 Future Improvements

Possible future features include:

* User authentication
* Saved jobs
* Search history
* Resume history
* Job filtering
* Salary filtering
* Remote/hybrid filtering
* Job matching scores
* Multiple job APIs
* Database integration
* Personalized user dashboard
* Deployment to a cloud platform

---

## 👨‍💻 Author

**Maanaz K Antony**

BTech Computer Science Engineering

Built as a practical AI/ML project using Python, CrewAI, Google Gemini, Streamlit, and the Adzuna Jobs API.
