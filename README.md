# AI-Based Internship Recommendation System

## 1. Project Title

**AI-Based Internship Recommendation System**

---

## 2. Project Overview

The **AI-Based Internship Recommendation System** is a web-based application developed to help students identify internship opportunities that are suitable for their academic background, technical skills, career interests, preferred location, preferred work mode, and stipend expectations.

The system uses a **hybrid internship recommendation approach** that combines text similarity, skill matching, career-domain matching, location preference, compensation preference, student suitability, and employer rating.

In addition to internship recommendations, the system provides:

- Student profile management
- Internship recommendation
- Skill matching
- Skill-gap analysis
- Personalized learning recommendations
- Skill assessment through quizzes
- Company internship posting
- Internship analytics

The system is designed as an academic project prototype demonstrating how Artificial Intelligence, Natural Language Processing, Machine Learning techniques, and data-driven recommendation methods can be applied to internship recommendation.

---

# 3. Problem Statement

Students often find it difficult to identify internship opportunities that match their technical skills, career interests, academic background, preferred location, and work preferences.

At the same time, companies need an efficient way to identify candidates whose skills and interests match their internship requirements.

Traditional internship searching generally requires students to manually search through many internship postings and compare requirements individually.

Therefore, there is a need for an intelligent system that can analyze student profiles and internship requirements and provide personalized internship recommendations.

---

# 4. Objectives

The main objectives of the project are:

1. To develop an AI-based system for recommending suitable internships to students.
2. To compare student skills with internship-required skills.
3. To identify skill gaps between students and internship requirements.
4. To recommend learning resources for missing skills.
5. To provide quizzes for evaluating student knowledge.
6. To allow companies to create internship opportunities.
7. To rank internships according to their suitability for a student.
8. To provide analytics related to internships and recommendations.
9. To provide a simple and user-friendly interface through Streamlit.

---

# 5. Key Features

## 5.1 Student Portal

The Student Portal provides:

- Student profile
- Academic details
- CGPA
- Technical skills
- Preferred career domain
- Preferred location
- Preferred work mode
- Expected stipend
- AI-based internship recommendations
- Recommendation score
- Matched skills
- Missing skills
- Skill-gap analysis

---

## 5.2 Company Portal

The Company Portal allows companies to:

- View company information
- Specify company industry
- Specify company location
- Post internship opportunities
- Specify internship role
- Specify required skills
- Specify internship domain
- Specify location
- Specify work mode
- Specify stipend
- Provide employer rating
- View available internships

---

## 5.3 Internship Recommendation

The system analyzes the student profile and available internship opportunities.

Each internship receives a recommendation score based on multiple factors.

The internships are then ranked according to their calculated score.

The highest-ranked internships are presented to the student as recommended opportunities.

---

## 5.4 Skill Matching

The system compares the skills possessed by the student with the skills required by an internship.

For example:

```text
Student Skills:
Python, SQL, Git

Required Skills:
Python, SQL, Pandas, Git

Matched Skills:
Python
SQL
Git

Missing Skill:
Pandas
```

This helps students understand how well their current skills match an internship.

---

## 5.5 Skill-Gap Analysis

The system identifies skills that are required by an internship but are not present in the student's profile.

The identified missing skills are used to generate personalized learning recommendations.

---

## 5.6 Personalized Learning Path

The Learning Path module connects missing skills with relevant learning resources.

The learning process is designed as:

```text
Missing Skill
      ↓
Recommended Learning Resource
      ↓
Practice
      ↓
Quiz
      ↓
Score
      ↓
Progress
```

The current prototype uses a course dataset containing information such as:

- Course name
- Skills covered
- Platform
- Difficulty level

---

## 5.7 Quiz Module

The Quiz module provides topic-based multiple-choice questions.

Features include:

- Topic selection
- Multiple-choice questions
- Automatic evaluation
- Score calculation
- Performance feedback

The quiz score is calculated using:

```text
Quiz Score =
(Number of Correct Answers / Total Questions) × 100
```

---

## 5.8 Analytics Dashboard

The Analytics module provides information about:

- Total internships
- Total recommendations
- Average recommendation score
- Internship distribution by domain
- Internship distribution by work mode
- Internship stipend distribution
- Internship dataset

The dashboard helps visualize the available internship data and recommendation information.

---

# 6. Hybrid Recommendation Algorithm

The system uses a hybrid recommendation approach.

The proposed weights are:

| Recommendation Component | Weight |
|---|---:|
| TF-IDF + Cosine Similarity | 35% |
| Skill Matching | 25% |
| Career/Domain Matching | 15% |
| Location Matching | 10% |
| Compensation Matching | 5% |
| Student Suitability | 5% |
| Employer Rating | 5% |
| **Total** | **100%** |

These weights represent the proposed hybrid recommendation design of the project.

They should be further evaluated and tuned using larger real-world datasets and user feedback before being considered production-validated weights.

---

# 7. Recommendation Components

## 7.1 TF-IDF and Cosine Similarity

TF-IDF is used to represent text information from student profiles and internship requirements.

Cosine similarity is then used to measure the similarity between the two text representations.

The cosine similarity formula is:

```text
Cosine Similarity(A,B) =
(A · B) / (||A|| × ||B||)
```

The resulting similarity value is converted into a percentage score.

---

## 7.2 Skill Matching

The system compares student skills with required internship skills.

The skill matching score is calculated as:

```text
Skill Coverage =
(Matched Required Skills / Total Required Skills) × 100
```

The system also produces:

- Matched skills
- Missing skills

---

## 7.3 Career/Domain Matching

The student's preferred career domain is compared with the internship domain.

For example:

```text
Student Domain:
Artificial Intelligence

Internship Domain:
Artificial Intelligence

Domain Match:
100%
```

---

## 7.4 Location Matching

The student's preferred location is compared with the internship location.

Remote internships can also satisfy location requirements where applicable.

---

## 7.5 Compensation Matching

The student's expected stipend is compared with the stipend offered by the internship.

Internships offering a stipend closer to or above the student's expectation receive a higher compensation score.

---

## 7.6 Student Suitability

The student's CGPA is considered as one of the suitability factors in the current prototype.

The suitability score is normalized to a percentage.

---

## 7.7 Employer Rating

Employer rating is incorporated into the recommendation score.

The current prototype uses a rating scale from 1 to 5.

The rating is normalized into a percentage before being included in the hybrid score.

---

# 8. Recommendation Workflow

The complete recommendation workflow is:

```text
Student Profile
       ↓
Student Skills and Preferences
       ↓
Internship Dataset
       ↓
TF-IDF Representation
       ↓
Cosine Similarity
       ↓
Skill Matching
       ↓
Domain Matching
       ↓
Location Matching
       ↓
Compensation Matching
       ↓
Student Suitability
       ↓
Employer Rating
       ↓
Hybrid Recommendation Score
       ↓
Internship Ranking
       ↓
Top Internship Recommendations
       ↓
Skill-Gap Analysis
       ↓
Learning Recommendations
```

---

# 9. Technology Stack

## Programming Language

- Python

## Frontend

- Streamlit

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-learn

## Natural Language Processing

- TF-IDF
- Cosine Similarity

## Data Storage

- CSV files

## Development Environment

- Visual Studio Code
- Python Virtual Environment

## Version Control

- Git
- GitHub

---

# 10. Project Structure

```text
AI-Based-Internship-Recommendation-System/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── students.csv
│   ├── internships.csv
│   ├── companies.csv
│   ├── courses.csv
│   └── quizzes.csv
│
├── modules/
│   ├── __init__.py
│   ├── data.py
│   ├── recommendation.py
│   ├── skill_matching.py
│   ├── learning.py
│   ├── quiz.py
│   ├── company.py
│   └── analytics.py
│
├── docs/
│
└── screenshots/
```

---

# 11. Description of Source Code

## app.py

The main Streamlit application.

It provides navigation between:

- Home
- Student Portal
- Company Portal
- Learning Path
- Quiz
- Analytics

---

## modules/data.py

Responsible for loading student and internship datasets.

---

## modules/recommendation.py

Implements the hybrid recommendation algorithm.

It calculates:

- TF-IDF similarity
- Skill matching
- Domain matching
- Location matching
- Compensation matching
- Student suitability
- Employer rating
- Final recommendation score

---

## modules/skill_matching.py

Responsible for comparing student skills and internship-required skills.

It identifies:

- Matched skills
- Missing skills
- Skill-match percentage

---

## modules/learning.py

Responsible for:

- Loading course information
- Identifying courses related to missing skills
- Generating learning recommendations

---

## modules/quiz.py

Responsible for:

- Loading quiz questions
- Filtering questions by topic
- Calculating quiz scores

---

## modules/company.py

Responsible for:

- Loading company information
- Adding internship records

---

## modules/analytics.py

Responsible for calculating recommendation and internship statistics.

---

# 12. Dataset

The current prototype uses CSV files.

## students.csv

Contains student information including:

- Student ID
- Name
- Degree
- Branch
- CGPA
- Skills
- Preferred domain
- Preferred location
- Preferred work mode
- Expected stipend

---

## internships.csv

Contains internship information including:

- Internship ID
- Company
- Role
- Domain
- Required skills
- Location
- Work mode
- Stipend
- Employer rating

---

## companies.csv

Contains:

- Company ID
- Company name
- Industry
- Location

---

## courses.csv

Contains:

- Course ID
- Course name
- Skills
- Learning platform
- Level

---

## quizzes.csv

Contains:

- Question ID
- Topic
- Question
- Option A
- Option B
- Option C
- Option D
- Correct answer

---

## Dataset Note

The datasets currently included in this repository are prototype/sample datasets created for demonstrating the functionality of the academic project.

They should not be considered a live or comprehensive internship database.

The system can be connected to a larger real-world dataset or internship API in future development.

---

# 13. System Requirements

The following software is required:

- Python 3.x
- pip
- Git
- Visual Studio Code
- Modern web browser

Recommended:

- Windows 10/11
- Minimum 4 GB RAM
- Stable internet connection for package installation

---

# 14. Installation

## Step 1: Clone the Repository

After the GitHub repository is created:

```bash
git clone <YOUR-GITHUB-REPOSITORY-LINK>
```

---

## Step 2: Open the Project Directory

```bash
cd AI-Based-Internship-Recommendation-System
```

---

## Step 3: Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

---

## Step 4: Activate the Virtual Environment

For PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

For Command Prompt:

```cmd
venv\Scripts\activate
```

After activation, the terminal should display:

```text
(venv)
```

---

# 15. Install Required Packages

Install all dependencies using:

```bash
pip install -r requirements.txt
```

The main packages used by the project are:

```text
streamlit
pandas
numpy
scikit-learn
matplotlib
```

---

# 16. Running the Application

Make sure the virtual environment is activated.

Run:

```bash
streamlit run app.py
```

If Streamlit is not recognized, use:

```bash
python -m streamlit run app.py
```

After successful execution, Streamlit will provide a local web address.

Open the displayed address in a web browser.

---

# 17. Application Navigation

The application contains the following main sections:

```text
Home
│
├── Student Portal
│
├── Company Portal
│
├── Learning Path
│
├── Quiz
│
└── Analytics
```

---

# 18. Student Portal Usage

1. Open the **Student Portal**.
2. Select a student from the available student records.
3. Review the student profile.
4. Review academic and skill information.
5. Click **Generate AI Recommendations**.
6. The system calculates recommendation scores.
7. Recommended internships are displayed in ranked order.
8. Open an internship recommendation to view:
   - Company
   - Role
   - Domain
   - Location
   - Work mode
   - Stipend
   - Skill match
   - Domain match
   - Location match
   - Matched skills
   - Missing skills

---

# 19. Company Portal Usage

1. Open the **Company Portal**.
2. Select a company.
3. View company information.
4. Open the internship posting form.
5. Enter the internship ID.
6. Enter the internship role.
7. Enter the domain.
8. Enter required skills.
9. Enter location.
10. Select work mode.
11. Enter stipend.
12. Enter employer rating.
13. Click **Post Internship**.

---

# 20. Learning Path Usage

1. Open **Learning Path**.
2. Select a student.
3. The system generates internship recommendations.
4. The highest-ranked internship is analyzed.
5. Missing skills are identified.
6. Courses related to missing skills are displayed.
7. The student can use these resources to improve the required skills.

---

# 21. Quiz Usage

1. Open the **Quiz** section.
2. Select a topic.
3. Answer the multiple-choice questions.
4. Click **Submit Quiz**.
5. The system calculates the score.
6. Feedback is displayed based on the obtained score.

---

# 22. Analytics Usage

The Analytics Dashboard displays:

- Total internships
- Total recommendations
- Average recommendation score
- Internships by domain
- Internships by work mode
- Internship stipend distribution
- Internship dataset

---

# 23. Testing

The application should be tested for the following areas:

### Student Portal

- Student selection
- Profile display
- Recommendation generation
- Recommendation ranking
- Skill matching
- Skill-gap identification

### Company Portal

- Company selection
- Internship form
- Required field validation
- Internship posting

### Learning Path

- Missing skill detection
- Course matching
- Learning resource display

### Quiz

- Topic selection
- Question display
- Answer selection
- Score calculation
- Feedback

### Analytics

- Statistics calculation
- Charts
- Dataset display

---

# 24. Screenshots

Application screenshots are stored in the `screenshots/` directory.

Recommended screenshots include:

1. Home Page
2. Student Portal
3. Student Profile
4. Internship Recommendations
5. Skill Matching
6. Skill-Gap Analysis
7. Company Portal
8. Internship Posting
9. Learning Path
10. Quiz
11. Quiz Result
12. Analytics Dashboard

These screenshots provide evidence of the implemented project functionality.

---

# 25. Limitations

The current implementation has the following limitations:

1. The prototype uses CSV files instead of a production database.
2. The internship dataset is limited in size.
3. The current recommendation weights are proposed and require further validation.
4. The application does not currently use live internship listings.
5. Authentication is not implemented as part of the current prototype.
6. The current company internship posting mechanism is intended for prototype demonstration.
7. Recommendation quality depends on the information available in the dataset.

---

# 26. Future Scope

The system can be enhanced in the future by:

- Integrating real-time internship APIs.
- Using larger real-world internship datasets.
- Implementing MySQL or PostgreSQL.
- Adding student and company authentication.
- Adding resume upload functionality.
- Extracting skills automatically from resumes using NLP.
- Developing advanced machine-learning ranking models.
- Adding feedback-based recommendation improvement.
- Adding email notifications.
- Adding internship application tracking.
- Adding student progress tracking.
- Adding company-side candidate recommendations.
- Adding multilingual support.
- Deploying the application on a cloud platform.
- Developing a mobile application.
- Adding explainable AI for recommendation decisions.

---

# 27. Project Workflow

The overall system workflow is:

```text
Student Registration/Profile
          ↓
Student Information
          ↓
Skills + Preferences + CGPA
          ↓
Internship Dataset
          ↓
Hybrid Recommendation Algorithm
          ↓
Internship Ranking
          ↓
Recommended Internships
          ↓
Skill-Gap Analysis
          ↓
Learning Recommendations
          ↓
Quiz Assessment
          ↓
Performance Feedback
```

---

# 28. Security and Data Considerations

The current project is an academic prototype and uses local CSV datasets.

No sensitive personal information should be added to the prototype datasets.

For production deployment, the system should implement:

- Secure authentication
- Password protection
- Database access controls
- Input validation
- Secure API communication
- Data encryption
- Privacy controls
- Role-based access control

---

# 29. Academic Project Information

**Project Title:** AI-Based Internship Recommendation System

**Project Type:** B.Tech CSE (AIML) Special Project

**Institution:** IFHE Hyderabad

**Department:** Computer Science and Engineering – Artificial Intelligence and Machine Learning

**Academic Year:** 2026–2027

**Project Guide:** Dr. Sukanta Das

---

# 30. Repository

The final source code will be available through the project's GitHub repository.

GitHub Repository:

```text
<ADD-FINAL-GITHUB-REPOSITORY-LINK-HERE>
```

---

# 31. Dataset and Related Resources

The prototype datasets are included inside the `data/` directory.

```text
data/
├── students.csv
├── internships.csv
├── companies.csv
├── courses.csv
└── quizzes.csv
```

If external datasets, APIs, or online resources are used in future versions, their official links should be documented here.

---

# 32. References

The project is based on concepts related to recommender systems, information retrieval, machine learning, explainable AI, and web application development.

Important references include:

1. Ricci, F., Rokach, L., & Shapira, B. *Recommender Systems Handbook*. 3rd Edition, 2022.

2. Manning, C. D., Raghavan, P., & Schütze, H. *Introduction to Information Retrieval*. Cambridge University Press, 2008.

3. Chen, T., & Guestrin, C. “XGBoost: A Scalable Tree Boosting System.” Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016.

4. Lundberg, S. M., & Lee, S.-I. “A Unified Approach to Interpreting Model Predictions.” Advances in Neural Information Processing Systems, 2017.

5. Streamlit Documentation.

6. Python Documentation.

7. Scikit-learn User Guide.

8. Roy, S., & Sharma, A. “AI-Powered Career Guidance.” IEEE Access, 2026.

9. Çelik Ertuğrul, D., & Bitirim, Y. “Job Recommender Systems: A Systematic Review.” Journal of Big Data, 2025.

10. Victoria et al. “AI-Based Internship Recommendation Engine for PM Internship Scheme.” ICESIC, 2026.

11. Panchasara et al. “AI Based Job Recommendation System using BERT.” ICCUBEA, 2023.

12. Chandrakumara, & Silva. “AI-Powered Hybrid Framework for Career Readiness,” 2026.

13. Guan et al. “JobFormer.” ACM Transactions on Knowledge Discovery from Data, 2024.

---

# 33. License

This project is developed for academic and educational purposes as part of the B.Tech CSE (AIML) Special Project.

---

## End of README