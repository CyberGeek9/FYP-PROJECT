# import os
# import json
# from typing import Dict, Any
# from openai import OpenAI
#
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#
# def ai_compare_resume_job(resume_text: str, job_text: str, max_tokens: int = 500) -> Dict[str, Any]:
#     """
#     Sends resume and job description text to OpenAI and returns parsed JSON:
#       - match_score (0–100)
#       - matched_skills (list[str])
#       - missing_skills (list[str])
#       - suggestions (list[str])
#       - short_summary (str)
#     """
#
#     system_prompt = (
#         "You are an expert recruitment assistant. "
#         "Given a resume and job description, output ONLY JSON:\n"
#         "{\n"
#         "  match_score: int,\n"
#         "  matched_skills: [strings],\n"
#         "  missing_skills: [strings],\n"
#         "  suggestions: [short strings],\n"
#         "  short_summary: string\n"
#         "}"
#     )
#
#     # Safely trim long text
#     MAX_CHARS = 25000
#     resume_snip = resume_text[:MAX_CHARS]
#     job_snip = job_text[:MAX_CHARS]
#
#     user_prompt = (
#         f"Resume:\n```\n{resume_snip}\n```\n\n"
#         f"Job description:\n```\n{job_snip}\n```\n\n"
#         "Return ONLY valid JSON output."
#     )
#
#     try:
#         resp = client.chat.completions.create(
#             model="gpt-4o-mini-2024-07-18",
#             messages=[
#                 {"role": "system", "content": system_prompt},
#                 {"role": "user", "content": user_prompt},
#             ],
#             max_tokens=max_tokens,
#             temperature=0.0
#         )
#
#         text = resp.choices[0].message.content.strip()
#
#         # Extract JSON only
#         start = text.find("{")
#         end = text.rfind("}")
#
#         if start == -1 or end == -1:
#             return {
#                 "match_score": 0,
#                 "matched_skills": [],
#                 "missing_skills": [],
#                 "suggestions": ["AI did not return JSON."],
#                 "short_summary": ""
#             }
#
#         json_text = text[start:end + 1]
#         data = json.loads(json_text)
#
#         # Guarantee all fields exist
#         data.setdefault("match_score", 0)
#         data.setdefault("matched_skills", [])
#         data.setdefault("missing_skills", [])
#         data.setdefault("suggestions", [])
#         data.setdefault("short_summary", "")
#
#         return data
#
#     except Exception as e:
#         return {
#             "match_score": 0,
#             "matched_skills": [],
#             "missing_skills": [],
#             "suggestions": [f"AI service error: {str(e)}"],
#             "short_summary": "AI service unavailable."
#         }
