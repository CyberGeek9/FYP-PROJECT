# import spacy
# import re
# from PyPDF2 import PdfReader
#
# # Load NLP model
# nlp = spacy.load("en_core_web_sm")
#
# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     reader = PdfReader(pdf_path)
#     for page in reader.pages:
#         text += page.extract_text() or ""
#     return text
#
# # Common skill keywords (you can expand this list)
# SKILL_KEYWORDS = [
#     "Python", "Java", "Machine Learning", "Deep Learning", "AI",
#     "Flask", "Django", "SQL", "Data Analysis", "Communication",
#     "Leadership", "HTML", "CSS", "JavaScript", "Testing",
#     "Automation", "Manual Testing", "Quality Assurance", "NLP"
# ]
#
# # Extract skills from text
# def extract_skills(text):
#     found = [skill for skill in SKILL_KEYWORDS if re.search(rf"\b{skill}\b", text, re.IGNORECASE)]
#     return list(set(found))
#
# # Compare resume and job description
# def compare_skills(resume_text, jobdesc_text):
#     resume_skills = extract_skills(resume_text)
#     job_skills = extract_skills(jobdesc_text)
#
#     matched = list(set(resume_skills) & set(job_skills))
#     missing = list(set(job_skills) - set(resume_skills))
#
#     score = int((len(matched) / len(job_skills)) * 100) if job_skills else 0
#
#     return {
#         "resume_skills": resume_skills,
#         "job_skills": job_skills,
#         "matched_skills": matched,
#         "missing_skills": missing,
#         "match_score": score
#     }
# def suggest_improvements(missing_skills):
#     suggestions = []
#     for skill in missing_skills:
#         if skill.lower() == "python":
#             suggestions.append("Improve Python by practicing data structures and automation projects.")
#         elif "testing" in skill.lower():
#             suggestions.append("Enhance Testing skills with Selenium or PyTest frameworks.")
#         elif "sql" in skill.lower():
#             suggestions.append("Work on SQL joins, queries, and database optimization.")
#         elif "communication" in skill.lower():
#             suggestions.append("Develop communication through team collaboration or online courses.")
#         else:
#             suggestions.append(f"Consider improving your {skill} skill through online learning or certification.")
#     return suggestions

