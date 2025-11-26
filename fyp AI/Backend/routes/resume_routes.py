# from flask import Blueprint, request, jsonify
# import os
#
# # Use package import path (project root should already be on sys.path)
# from Backend.utils.openai_integration import ai_compare_resume_job
# from Backend.utils.text_processing import extract_text  # uses your existing extractor
#
# resume_routes = Blueprint('resume_routes', __name__)
#
# UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#
#
# @resume_routes.route('/analyze_batch', methods=['POST'])
# def analyze_batch():
#     # Check files
#     if 'resumes' not in request.files:
#         return jsonify({"error": "No resumes uploaded"}), 400
#
#     uploaded_files = request.files.getlist("resumes")
#     jobdesc = request.form.get("jobdesc", "")
#
#     if not jobdesc.strip():
#         return jsonify({"error": "Job description required"}), 400
#
#     results = []
#
#     for resume in uploaded_files:
#         # prevent empty filename
#         if not resume or resume.filename == "":
#             continue
#
#         save_path = os.path.join(UPLOAD_FOLDER, resume.filename)
#         resume.save(save_path)
#
#         # Extract text from the saved resume (PDF/DOCX)
#         try:
#             resume_text = extract_text(save_path)
#         except Exception as e:
#             # fallback: store error for this resume
#             results.append({
#                 "filename": resume.filename,
#                 "error": f"Failed to extract text: {str(e)}"
#             })
#             continue
#
#         # Call OpenAI helper (returns dict with match_score, matched_skills, missing_skills, suggestions, short_summary)
#         ai_result = ai_compare_resume_job(resume_text, jobdesc, max_tokens=700)
#
#         # Normalize keys (safe access)
#         results.append({
#             "filename": resume.filename,
#             "match_score": ai_result.get("match_score", 0),
#             "matched_skills": ai_result.get("matched_skills", []),
#             "missing_skills": ai_result.get("missing_skills", []),
#             "suggestions": ai_result.get("suggestions", []),
#             "short_summary": ai_result.get("short_summary", "")
#         })
#
#     # sort by match_score desc
#     results_sorted = sorted(results, key=lambda x: x.get("match_score", 0), reverse=True)
#
#     return jsonify({"results": results_sorted})

