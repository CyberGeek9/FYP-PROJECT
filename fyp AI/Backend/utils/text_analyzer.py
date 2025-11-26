# import re
# import spacy
#
# # Load Spacy model
# nlp = spacy.load("en_core_web_sm")
#
# def extract_skills(text):
#     """
#     Extracts relevant skills from resume text using keyword matching.
#     """
#     skills_list = [
#         "Python", "Java", "C++", "HTML", "CSS", "JavaScript",
#         "Flask", "Django", "Machine Learning", "Deep Learning",
#         "Data Analysis", "SQL", "Communication", "Leadership",
#         "Problem Solving", "Teamwork"
#     ]
#
#     found_skills = [
#         skill for skill in skills_list
#         if re.search(rf"\b{skill}\b", text, re.IGNORECASE)
#     ]
#     return found_skills
#
#
# def analyze_resume_text(text):
#     """
#     Uses spaCy for named entity recognition and combines with extracted skills.
#     """
#     doc = nlp(text)
#     entities = [(ent.text, ent.label_) for ent in doc.ents]
#
#     skills = extract_skills(text)
#
#     return {
#         "skills": skills,
#         "entities": entities
#     }
