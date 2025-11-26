# import os
# import PyPDF2
# import docx2txt
#
# def extract_text_from_pdf(file_path):
#     text = []
#     try:
#         with open(file_path, 'rb') as f:
#             reader = PyPDF2.PdfReader(f)
#             for page in reader.pages:
#                 text.append(page.extract_text() or "")
#         return "\n".join(text)
#     except Exception as e:
#         print("PDF extraction error:", e)
#         return ""
#
# def extract_text_from_docx(file_path):
#     try:
#         text = docx2txt.process(file_path)
#         return text if text else ""
#     except Exception as e:
#         print("DOCX extraction error:", e)
#         return ""
#
# def extract_text(file_path):
#     """Automatically detect file type and extract text"""
#     if not os.path.exists(file_path):
#         return ""
#     ext = os.path.splitext(file_path)[1].lower()
#     if ext == ".pdf":
#         return extract_text_from_pdf(file_path)
#     elif ext in [".docx", ".doc"]:
#         return extract_text_from_docx(file_path)
#     else:
#         # if plain text file
#         try:
#             with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
#                 return f.read()
#         except Exception as e:
#             print("Text extraction error:", e)
#             return ""
